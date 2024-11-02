# создадим класс Rectangle, который вычисляет его площадь и сумму площадей
# создать класс Square, который вычисляет его площадь и сумму площадей
# объединить все в класс Figure(абстрактный класс)  - Пересмотрел видео так и не понял как пользоваться нужно
# класс круг передаем радиус, который вычисляет его площадь
from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sum_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        super().__init__(name)
        if side_a <= 0 or side_b <= 0:
            raise ValueError('Стороны прямоугольника не могут быть отрицательными и равным 0')
        self.side_b = side_b
        self.side_a = side_a

    '''Вычисление плошади'''

    def get_rect_area(self):
        return self.side_a * self.side_b

    '''Сумма площадей'''

    def sum_area(self, area):
        if area <= 0:
            raise ValueError('Сумма площади Прамоугольника должна быть больше 0')

        return self.get_rect_area() + self.get_rect_area()


class Square(Figure):
    def __init__(self, side_a, name):
        super().__init__(name)
        if side_a <= 0:
            raise ValueError('Сторона квадрата должна быть положительной и != 0')
        self.side_a = side_a

    '''Вычисление плошади'''

    def get_sqr_area(self):
        return self.side_a ** 2

    '''Сумма площадей'''

    def sum_area(self, area):
        if area <= 0:
            raise ValueError('Сумма площади Квадрата должна быть больше 0')

        return self.get_sqr_area() + self.get_sqr_area()


class Circle(Figure):
    def __init__(self, radius, name):
        super().__init__(name)
        if radius <= 0:
            raise ValueError('Сторона квадрата должна быть положительной и != 0')

        self.radius = radius

    '''Вычисление плошади'''

    def get_circle_area(self):
        return 3.14 * self.radius ** 2

    '''Сумма площадей'''

    def sum_area(self, area):
        if area <= 0:
            raise ValueError('Сумма площади Квадрата должна быть больше 0')

        return self.get_circle_area() + self.get_circle_area()
