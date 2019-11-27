"""Contains a base class for all the formatter classes"""
from abc import ABC, abstractmethod


class BaseOutputFormatter(ABC):
    """Serves as a base class for all the formatter classes"""

    def __init__(self):
        self._result = None

    @property
    def result(self):
        """Getter for result"""
        return self._result

    @result.setter
    def result(self, result):
        """Setter for result"""
        self._result = result

    @abstractmethod
    def convert(self):
        """Converts result data to a various format"""
        raise NotImplementedError

    @abstractmethod
    def get_converted_result(self):
        """Returns converted result"""
        raise NotImplementedError
