#!/usr/bin/python3
"""
Module contains a main class that runs tests
"""
import importlib
import os
import sys
import traceback

from dodo.introspector import Introspector


class Dodo(object):
    """Main class that contains a logic to run tests"""

    # Result constants
    RESULT_CONSTANTS = {0: "Fail", 1: "Pass"}

    def __init__(self, package_directory, test_regex=None, testplan=None):
        """Init method"""
        self._package_dir = package_directory

        # Store test function name with result pass/fail. We store 0 for
        # Failed and 1 for Pass
        self._functions_results = dict()

        # Dictionary with {<module_name>:<[functions]>}
        self._module_functions = dict()

        self._testregex = test_regex
        self._testplan = testplan

    def execute_tests(self):
        """Execute tests"""
        # TODO: Use Python 3 Path module

        # Get the absolute path of supplied directory in case only directory
        # name is supplied instead of full path
        absolute_path = os.path.abspath(self._package_dir)

        # Parent directory is a parent directory of a package. i.e In
        # /tmp/testdir, /tmp is a parent directory
        parent_dir = os.path.normpath(os.path.join(absolute_path, ".."))

        # We need to put parent directory of package in PYTHONPATH to import it
        sys.path.append(parent_dir)

        # Get the basename of path. i.e In /tmp/testdir, testdir is a base name
        package_name = os.path.basename(absolute_path)

        # NOTE: Introspector.find_modules method doesn't retrieve modules
        # from top level directory of a package, so We need to process that
        # separately.

        # Import package dynamically to get modules in top level directory
        package_instance = importlib.import_module(package_name)

        # Get modules from top level package directory
        modules = Introspector.get_modules_from_package(package_instance)

        # Get modules recursively
        all_modules = Introspector.find_modules(self._package_dir)
        modules.extend(all_modules)

        # Get functions from all the modules
        self._module_functions = self._populate_module_functions_list(
            modules, package_name)

        self._functions_results = self._execute_test_functions(
            self._module_functions)

    def _populate_module_functions_list(self, modules, package_name):
        """Iterate through all the modules and return dictionary with
           <module-name>:<[functions]>
        """
        module_functions = dict()
        module_functions_get = module_functions.get
        for module in modules:
            try:
                tmp = importlib.import_module(
                    "{0}.{1}".format(package_name, module))
                functions = Introspector.get_functions_from_module(
                    tmp, self._testregex, self._testplan)
                function_list = module_functions_get(module, [])
                function_list.extend(functions)
                module_functions[module] = function_list
            except Exception as _:
                exc_type, exc_value, exc_tb = sys.exc_info()
                print("".join(
                    (traceback.format_exception(exc_type, exc_value, exc_tb))))
        return module_functions

    def _execute_test_functions(self, module_functions):
        """Iterate through module_functions dictionary and execute each
           function for all the modules.
        """
        results = dict()
        for _, function_list in module_functions.items():
            for function in function_list:
                try:
                    # Execute function
                    function[1]()
                    results[function[1].__name__] = 1
                except Exception:
                    exc_type, exc_value, exc_tb = sys.exc_info()
                    print("".join(
                        (traceback.format_exception(
                            exc_type, exc_value, exc_tb)))
                         )
                    results[function[1].__name__] = 0
        return results

    def get_result(self):
        """Returns a dictionary of <function-name>:<0|1>"""
        return self._functions_results

    @staticmethod
    def print_usage():
        """Print usage information"""
        print("dodo is a simple test framework used to write tests for Python \
            application")
        print("dodo <test-directory>")
