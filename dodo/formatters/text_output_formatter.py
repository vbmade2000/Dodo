"""Contains a formatter class to convert result to text format"""


from dodo.formatters import base_output_formatter


class TextFormatter(base_output_formatter.BaseOutputFormatter):
    """Converts result to Text format"""

    def __init__(self):
        """Initialize class"""
        super(TextFormatter, self).__init__()
        self._result = None
        self._converted_result = None

    def convert(self):
        """Overriden method that converts result to text format"""
        self._converted_result = self._result

    def get_converted_result(self):
        """Overriden method that returns a result converted into text
           format.
        """
        return self._converted_result
