#!/usr/bin/python3
"""module documantation"""


class Square:
    """a Square class with size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize the size attribute
        Args:
            size (int): the size of the square
            value (tuple): the coordinates for position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """gets the value of position attribute
        Return:
              the value of position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position attribute
        Args:
            value (tuple): the value to set
        """
        if type(value) is tuple and len(value) == 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculates the area of the square
        Args:
            self.__size (int): the side of the square
        Return:
            the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """prints the square to stdout
        Return: None
        """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
