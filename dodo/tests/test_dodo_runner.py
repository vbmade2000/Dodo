"""Unit tests for Dodo class"""

import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock

from dodo.dodo_runner import Dodo


class TestDodo(TestCase):
    """
     Unit tests for Dodo class
    """

    @patch("dodo.dodo_runner.os")
    @patch("dodo.dodo_runner.sys")
    @patch("dodo.dodo_runner.importlib")
    @patch("dodo.dodo_runner.Introspector")
    def test_execute(self, mock_introspector, mock_importlib,
                     mock_sys, mock_os):
        """Test execute method"""
        # ---- Prepare
        package_name = "test"
        package_dir = "/some/test/path"
        dodo = Dodo(package_dir, None, None)

        # Specify return values for methods in os package
        mock_os.path.abspath.return_value = package_dir
        mock_os.path.join.return_value = "/some/test/path/.."
        mock_os.path.normpath.return_value = "/some/test"
        mock_os.path.basename.return_value = package_name

        # Specify return values for methods in importlib package
        mock_importlib.import_module.return_value = MagicMock()

        # ---- Execute
        dodo.execute_tests()

        # ---- Verify
        mock_os.path.abspath.assert_called_with(package_dir)
        mock_os.path.join.assert_called_with(package_dir, "..")
        mock_os.path.normpath.assert_called_with("/some/test/path/..")
        mock_sys.path.append.assert_called_with("/some/test")
        mock_os.path.basename.assert_called_with("/some/test/path")
        mock_importlib.import_module.assert_called_with(package_name)
        mock_introspector.get_modules_from_package.assert_called_with(
            mock_importlib.import_module.return_value)
        mock_introspector.find_modules.assert_called_with(package_dir)


if __name__ == "__main__":
    unittest.main()
