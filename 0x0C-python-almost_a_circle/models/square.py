#!/usr/bin/python3
"""module documentation"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """a class that inherits from the rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """instant initi"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, data):
        self.height = data
        self.width = data

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.height}'
