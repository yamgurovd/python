# Урок 1
# создадим класс Rectangle, который вычисляет его площадь и сумму площадей
# создать класс Square, который вычисляет его площадь и сумму площадей
# объединить все в класс Figure(абстрактный класс)  - Пересмотрел видео так и не понял как пользоваться нужно
# класс круг передаем радиус, который вычисляет его площадь
# ------------------------------------------------------------------------------------------------------------
# Урок 2
# суперфункция, которая будет проверять ошибки данных у всех классов
from abc import ABC, abstractmethod


def except_error(side_a=1, side_b=1, side_c=1, side_d=1, side=1, radius=1):
    if any([side_a is str, side_b is str, side_c is str, side_d is str, side is str, radius is str]):
        raise TypeError('Значения не должен быть Str формат')

    if any([side_a is None, side_b is None, side_c is None, side_d is None, side is None, radius is None]):
        raise TypeError('Значения не должен быть Nonetype формат')

    if any([side_a is bool, side_b is bool, side_c is bool, side_d is bool, side is bool, radius is bool]):
        raise TypeError('Значения не должен быть Bool формат')

    if any([side_a <= 0, side_b <= 0, side <= 0, side_c <= 0, side_d <= 0, radius <= 0]):
        raise ValueError('Стороны прямоугольника не могут быть отрицательными и равным 0')


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    def get_area(self):
        pass

    def example(self, a):
        if isinstance(a, Figure):
            raise ValueError(f'{a} не является вложенным классом')
        return a * 10

    def sum_area(self, area):
        if isinstance(area, ABC):
            raise ValueError(f"{area}", 'Не является вложенным классом Figure')
        self.area = area

        return self.get_area() + self.area.get_area()


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        super().__init__(name=name)
        except_error(side_a, side_b)

        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b


class Circle(Figure):
    def __init__(self, radius, name):
        super().__init__(name=name)
        except_error(radius)
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2


class Square(Figure):
    def __init__(self, side, name):
        super().__init__(name=name)
        if side <= 0:
            raise ValueError('Сторона квадрата не должна быть отрицательным равным 0')
        elif side is str:
            raise TypeError('Значения не должны быть текстовый формат')

        self.side = side

    def get_area(self):
        return self.side ** 2


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c, name):
        super().__init__(name=name)
        if any([side_a <= 0,
                side_b <= 0,
                side_c <= 0]):
            raise ValueError('Сторонs треугольника не должны быть отрицательным равным 0')

        elif any([side_a is str,
                  side_b is str,
                  side_c is str]):
            raise TypeError('Значения не должны быть текстовый формат')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return self.side_a + self.side_b + self.side_c


class Romb(Figure):
    def __init__(self, side_a, side_b, side_c, side_d, name):
        super().__init__(name=name)
        if any([side_a <= 0, side_b <= 0,
                side_c <= 0, side_d <= 0]):
            raise ValueError('Стороны ромба не должны быть отрицательным и равным 0')

        elif any([side_a is str,
                  side_b is str,
                  side_c is str,
                  side_d is str]):
            raise TypeError('Значения не должны быть текстовый формат')

        self.side_d = side_d
        self.side_c = side_c
        self.side_b = side_b
        self.side_a = side_a

    def get_area(self):
        return (self.side_a * self.side_b * self.side_c * self.side_d) / 2


# fig_dict = [Rectangle(1, 2, 'R'), Circle(1, 'C'),
#             Square(5, 'S'), Triangle(1, 2, 3, 'T'),
#             Romb(1, 2, 3, 4, 'Romb')]
#
# area_fig = [i.get_area() for i in fig_dict]
#
# print(f"Площади фигур: {area_fig}")
#
# exam_fig = [i.example('A') for i in fig_dict]
#
# print(f"Тестовый метод: {exam_fig}")
#
# sum_fig = [i.sum_area(i) for i in fig_dict]
#
# print(f"Сумма фигур: {sum_fig}")

#
# r = Rectangle(1, 156, "R")
# # c = Circle(3.14, "C")
# print(r.get_area())
# # print(c.get_area())
