import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import sys

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) < (other.x, other.y)
        raise NotImplementedError("Ошибка")

    def absolute(self):
        return Point(abs(self.x), abs(self.y))

    def round_point(self):
        return Point(float(round(self.x, 3)), float(round(self.y, 3)))


