# Написать класс Vector с двумя полями x and y type int
# Реализовать возможность сложения двух объектов класса Вектор через оператор сложения "+"
# В результате сложения получается новый объект класса Вектор
# Реализовать возможность сравнить два объекта класса Vector чере оператор сравнения "=="

print("Написать класс Vector c реализацией сложения и сравнения объектов")


class Vector:
    def __init__(self, x: int, y: int, ) -> None:
        self.x = x
        self.y = y
    @staticmethod
    def sum_vectors(vector1, vector2):
        new_vector = (vector1.x + vector2.x, vector1.y + vector2.y)

        return new_vector


    def equal(self,):


v1 = Vector(x=1, y=1)
v2 = Vector(x=4, y=-5)

v3 = Vector.sum_vectors(vector1=v1, vector2=v2)

