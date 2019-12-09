import unittest
from io import StringIO
from unittest.mock import patch

from dodo.color_printer import ColorPrinter


class TestColorPrinter(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_red(self, mock_stdout):
        """Test print_red method of ColorPrinter class"""
        expected_output = "\x1b[1m\x1b[31mTest text\x1b[0m\n"
        ColorPrinter.print_red("Test text")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_red(self, mock_stdout):
        """Test print_green method of ColorPrinter class"""
        expected_output = "\x1b[1m\x1b[32mTest text\x1b[0m\n"
        ColorPrinter.print_green("Test text")
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
