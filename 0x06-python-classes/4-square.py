#!/usr/bin/python3
"""module documantation"""


class Square:
    """a Square class with size attribute"""
    def __init__(self, size=0):
        """initialize the size attribute
        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """gets the size attribute
        Return:
              the size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """sets the size attribute
        Args:
            size (int): the size of the square
        Raises:
              ValueError: if size < 0
              TypeError: if size is not an integer
        Return:
              None
        """
        if type(size) is int and size >= 0:
            self.__size = size
        elif type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """calculates the area of the square
        Args:
            self.__size (int): the side of the square
        Return:
            the area of the square
        """
        return self.__size * self.__size
