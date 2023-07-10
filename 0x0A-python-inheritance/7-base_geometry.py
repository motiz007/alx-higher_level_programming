#!/usr/bin/python3
"""module documentation"""


class BaseGeometry:
    """a base geometry class"""
    def area(self):
        """raises an exception error
        Raises:
              Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer
        Args:
            name (str): the name
            value (int): the value to validate
        Raises:
              TypeError: {} must be an integer".format(self.name)
              ValueError: {} must be greater than 0".format(self.name)
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
