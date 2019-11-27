"""Contains a formatter class to convert result to JSON format"""

import json

from dodo.formatters import base_output_formatter


class JSONFormatter(base_output_formatter.BaseOutputFormatter):
    """Converts result to JSOn format"""

    def __init__(self):
        """Initialize class"""
        super(JSONFormatter, self).__init__()
        self._result = None
        self._converted_result = None

    def convert(self):
        """Overriden method that converts result to JSON format"""
        self._converted_result = json.dumps(self._result, indent=2)

    def get_converted_result(self):
        """Overriden method that returns a result converted into JSON
           format.
        """
        return self._converted_result
