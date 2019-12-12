"""Module contains test methods for Introspector class"""

import re
import types
import unittest
from unittest.mock import MagicMock, patch

from dodo.introspector import Introspector


class TestIntrospector(unittest.TestCase):
    """Class contains methods to test Intropector class"""

    def test_get_modules_from_package(self):
        """Test get_modules_from_package method"""
        with patch("dodo.introspector.pkgutil") as mock_pkgutil:
            mock_package = MagicMock()
            fake_path = "/some/fake/path"
            mock_package.__path__ = fake_path
            modules = Introspector.get_modules_from_package(mock_package)
            mock_pkgutil.iter_modules.assert_called_with(fake_path)
            self.assertEqual(type(modules), list)

    def test_get_functions_from_module_with_all(self):
        """Test get_functions_from_module method when Testplan or Test RegEx
           is not supplied.
        """
        # Mock module to pass to get_functions_from_module
        mock_module_object = MagicMock()

        # List to serve as a return value of inspect.getmember containing
        # mixed types.
        function_list = [("test1", lambda: 2*2)]

        # Patch inspect module
        with patch("dodo.introspector.inspect") as mock_inspect:
            mock_inspect.getmembers = MagicMock()
            mock_inspect.getmembers.return_value = function_list
            actual_value = Introspector.get_functions_from_module(
                mock_module_object, None, None)
            mock_inspect.getmembers.assert_called_with(mock_module_object)
            self.assertEqual(mock_inspect.isfunction.call_count, 1)
            self.assertEqual(len(actual_value), 1)
            self.assertEqual(
                isinstance(actual_value[0][1], types.FunctionType), True)

    def test_get_functions_from_module_with_regex(self):
        """Test get_functions_from_module method when test regex is supplied"""
        # Mock module to pass to get_functions_from_module
        mock_module_object = MagicMock()

        # Compiled RgEx object to be used to select test functions
        test_regex = re.compile(r"test_file_*")

        # List to serve as a return value of inspect.getmember containing
        # mixed types.
        function_list = [("test_network_connectivity", lambda: 2*2),
                         ("test_file_existence", lambda: 2*2),
                         ("test2", "string_type")]

        # Patch inspect module
        with patch("dodo.introspector.inspect") as mock_inspect:
            mock_inspect.getmembers = MagicMock()
            mock_inspect.getmembers.return_value = function_list
            actual_value = Introspector.get_functions_from_module(
                mock_module_object, test_regex, None)
            mock_inspect.getmembers.assert_called_with(mock_module_object)
            self.assertEqual(len(actual_value), 1)
            self.assertEqual(actual_value[0][0], "test_file_existence")
            self.assertEqual(
                isinstance(actual_value[0][1], types.FunctionType), True)

    def test_get_functions_from_module_with_testplan(self):
        """Test get_functions_from_module method when test regex is supplied"""
        # Mock module to pass to get_functions_from_module
        mock_module_object = MagicMock()

        # Testplan to be used to select test functions
        test_plan = ["test_network_connectivity"]

        # List to serve as a return value of inspect.getmember containing
        # mixed types.
        function_list = [("test_network_connectivity", lambda: 2*2),
                         ("test_file_existence", lambda: 2*2),
                         ("test2", "string_type")]

        # Patch inspect module
        with patch("dodo.introspector.inspect") as mock_inspect:
            mock_inspect.getmembers = MagicMock()
            mock_inspect.getmembers.return_value = function_list
            actual_value = Introspector.get_functions_from_module(
                mock_module_object, None, test_plan)
            mock_inspect.getmembers.assert_called_with(mock_module_object)
            self.assertEqual(len(actual_value), 1)
            self.assertEqual(actual_value[0][0], "test_network_connectivity")
            self.assertEqual(
                isinstance(actual_value[0][1], types.FunctionType), True)

    def test_find_modules(self):
        """Test find_modules method"""
        test_path = "/some/test/path"
        find_packages_return_value = [
            "/test/path1", "/test/path2", "/test/path3"]

        # Patch setuptools module
        with patch("dodo.introspector.find_packages") as mock_find_packages,\
                patch("dodo.introspector.iter_modules") as mock_iter_modules:
            mock_find_packages.return_value = find_packages_return_value
            actual_output = Introspector.find_modules(test_path)
            self.assertEqual(set(find_packages_return_value), actual_output)
            self.assertEqual(mock_find_packages.call_count, 1)
            self.assertEqual(mock_iter_modules.call_count, len(find_packages_return_value))



if __name__ == "__main__":
    unittest.main()
