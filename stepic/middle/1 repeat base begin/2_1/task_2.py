"""Индекс массы тела
Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека.
ИМТ показывает весит человек больше или меньше нормы для своего роста.
ИМТ человека рассчитывают по формуле:ИМТ=(рост(м)×рост(м))/масса (кг)

где масса измеряется в килограммах, а рост — в метрах.

Масса человека считается оптимальной,
если его ИМТ находится между 18.5 и 25.
Если ИМТ меньше 18.5, то считается, что человек весит ниже нормы.
Если значение ИМТ больше 25, то считается, что человек весит больше нормы.

Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.5 и 25 (включительно).
"Недостаточная масса", если ИМТ меньше 18.5 и "Избыточная масса", если значение ИМТ больше 25.

Формат входных данных
На вход программе подается два числа: масса и рост человека, каждое на отдельной строке.
Все входные числа являются вещественными, используйте для них тип данных float.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""
m, w = map(float, input().split())
print(m, w)
imt = m / (w ** 2)

if 25 < imt:
    print("Избыточная масса")
elif 15.5 > imt:
    print("Недостаточная масса")
else:
    print("Оптимальная масса")


# Второй способ решения задачи - взято из форума (особенность в ООП)
class Human():
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    @staticmethod
    def check(value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("Значение роста и веса человека должно быть неотрицательным числом")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height_value):
        self.check(height_value)
        self.__height = height_value
        self.__body_mass_index = None

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight_value):
        self.check(weight_value)
        self.__weight = weight_value
        self.__body_mass_index = None

    @property
    def body_mass_index(self):
        if self.__body_mass_index is None:
            self.__body_mass_index = self.weight / self.height ** 2
        return self.__body_mass_index

    def display_bmi(self):
        if self.body_mass_index < 18.5:
            print("Недостаточная масса")
        elif self.body_mass_index > 25:
            print("Избыточная масса")
        else:
            print("Оптимальная масса")


weight, height = float(input()), float(input())
Human(height, weight).display_bmi()

# Третий способ решения задачи - взято из форума
imt = float(input()) / float(input()) ** 2
print(('Оптимальная', 'Избыточная', 'Недостаточная')[(imt > 25) - (imt < 18.5)], 'масса')
