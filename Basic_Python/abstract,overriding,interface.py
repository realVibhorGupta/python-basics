# this is an interface because it has no implementation
from abc import abstractmethod, ABCMeta


class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super(Rectangle,
              self).__init__()
