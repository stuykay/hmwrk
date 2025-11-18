from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area():
        pass
    @abstractmethod
    def calculate_perimeter():
        pass
    def info():
        return "Какая-то фигура"

class Square(Shape):
    def __init__(self, side, square=0, perimeter=0):
        self.side = side
        self.square = square
        self.perimeter = perimeter
    def calculate_area(self):
        self.square = self.side**2
        return self.square
    def calculate_perimeter(self):
        self.perimeter = self.side*4
        return self.perimeter
    def info():
        return "Квадрат"
    def __str__ (self):
        return f'Квадрат со стороной {self.side} см'
    def __len__(self):
        return int(self.calculate_perimeter())
    def __eq__(self, other):
        return int(self.calculate_area()) == int(other.calculate_area())

class Circle(Shape):
    def __init__(self, radius, square=0, perimeter=0):
        self.radius = radius
        self.square = square
        self.perimeter = perimeter
    def calculate_area(self):
        self.square = (self.radius**2)*3.14
        return self.square
    def calculate_perimeter(self):
        self.perimeter = self.radius*2*3.14
        return self.perimeter
    def info():
        return "Круг"
    def __str__ (self):
        return f'Круг с радиусом {self.radius} см'
    def __len__(self):
        return int(self.calculate_perimeter())
    def __eq__(self, other):
        return int(self.calculate_area()) == int(other.calculate_area())

square1 = Square(8)
square2 = Square(9)
square3 = Square(9)
circle = Circle(4)

print(square1==square2)
print(square3==square2)
print(circle)
print(len(circle))

class GeometryCalculator:
    @staticmethod
    def validate_positive(number):
        if number > 0: return True
        else: return False
    @staticmethod
    def calculate_diagonal(length, width):
        return (length**2+width**2)**0.5
    @staticmethod
    def is_larger(shape1, shape2):
        return max(shape1, shape2)

print(GeometryCalculator.validate_positive(9))
print(GeometryCalculator.validate_positive(-1))
print(GeometryCalculator.calculate_diagonal(4,2))
print(GeometryCalculator.is_larger(square1.square, square3.square))