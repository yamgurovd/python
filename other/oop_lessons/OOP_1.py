class A:
    a = 1
    b = 2

    c = a + b


a = A()

print(a.c)
"""Абстракция """


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # Полиморфизм
    def add (self, figure):
        if isinstance(figure, Rectangle):
            raise ValueError("Значение параметра figure должен относится к Rectangle и наследующим классам")
        return self.width + figure.width


example1 = Rectangle(width=5, height=5)

"""Наследование"""


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def get_area(self):
        return self.side * self.side

example2 = Square(side=2)

print(example2.get_area())


"""Полиморфизм"""
example3 = Square(5).add(figure=5)


