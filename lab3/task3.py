from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def print_shape_info(self):
        print(f"Периметр фигуры: {self.perimeter()}")
        print(f"Площадь фигуры: {self.area()}")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        if width <= 0 or height <= 0:
            raise ValueError("Значение должно быть положительным числом.")
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Значение должно быть положительным числом.")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Значение должно быть положительным числом.")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Сумма длин двух сторон треугольника должна быть больше длины третьей стороны.")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a+self.b+self.c
    
    def area(self):
        p = (self.a + self.b + self.c)/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
  
    
second = Rectangle(3,4) # обрабатываю не все возможные ошибки, но это не точно
third = Circle(5) # не вызывать ничего для Shape
forth = Triangle(2, 3, 4)
second.print_shape_info()
third.print_shape_info()
forth.print_shape_info()
