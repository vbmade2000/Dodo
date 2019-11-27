"""Factory to create Formatter object"""
from dodo.formatters import json_output_formatter, text_output_formatter


class FormatterFactory:
    """Factory class to create Formatter object"""

    @staticmethod
    def get_formatter(formatter_name):
        """Returns object of a formatter class based on <formatter_name>"""
        formatter_name = formatter_name.upper()
        formatter_class_name = f"{formatter_name}Formatter"
        if formatter_class_name == "JSONFormatter":
            return json_output_formatter.JSONFormatter()
        elif formatter_class_name == "TEXTFormatter":
            return text_output_formatter.TextFormatter()
