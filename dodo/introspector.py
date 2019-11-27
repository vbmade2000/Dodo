"""Module provides functionality to introspect package"""

import inspect
import pkgutil
from pkgutil import iter_modules
from setuptools import find_packages


class Introspector(object):
    """Provides functionality to introspect python packages and modules"""

    def __init__(self):
        """Init method"""
        super().__init__()

    @staticmethod
    def get_modules_from_package(package_obj):
        """Extracts all the modules from <package_obj> using pkgutil and
           returns them. pkgutil.iter_items() returns output in format
           [(FileFinder("/tmp/testdir"), "best", True),
            (FileFinder("/tmp/testdir"), "test", False),
            (FileFinder("/tmp/testdir"), "test1", False)].
           It is a named tuple in format
           (importer, <package-name/module-name>, bool(ispackage)).
        """
        modules = [name for _, name, ispkg in
                   pkgutil.iter_modules(package_obj.__path__) if not ispkg]
        return modules

    @staticmethod
    def get_functions_from_module(module_obj):
        """Extracts all the functions from <module_obj> using introspection API
           and returns them.
           Example of return value of inspect.getmembers is following one.
           [("test1", <function test1 at 0x7f1e2761a7b8>),
            ("test2", <function test2 at 0x7f1e2761a840>)]
        """
        functions = [member for member in
                     inspect.getmembers(module_obj)
                     if inspect.isfunction(member[1])]
        return functions

    @staticmethod
    def find_modules(path):
        """Extract modules from <path> recursively using functionality from
           setuptools.
           NOTE: It doesn't extract modules from top level directory
           of a package.
        """
        modules = set()
        for pkg in find_packages(path):
            modules.add(pkg)
            pkgpath = path + '/' + pkg.replace('.', '/')
            for _, name, ispkg in iter_modules([pkgpath]):
                if not ispkg:
                    modules.add(pkg + '.' + name)
        return modules
