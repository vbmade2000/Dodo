"""Module contains a functionality to print colored text"""


class ColorPrinter(object):
    """Contains constants for text colors and methods to print colored text"""
    # pylint: disable=too-few-public-methods

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[32m"
    WARNING = "\033[93m"
    FAIL = "\033[31m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    @staticmethod
    def print_red(text):
        """Prints <text> in Red color on console
           TODO: Use Python3.6 f-string here
        """
        print(ColorPrinter.BOLD + ColorPrinter.FAIL + text + ColorPrinter.ENDC)

    @staticmethod
    def print_green(text):
        """Prints <text> in Green color on console
           TODO: Use Python3.6 f-string here
        """
        print(
            ColorPrinter.BOLD + ColorPrinter.OKGREEN +
            text + ColorPrinter.ENDC)
