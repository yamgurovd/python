"""
Средние значения
В математике выделяют следующие средние значения:
среднее арифметическое чисел a и b b: (a+b)/2;
среднее геометрическое чисел a и b: корень a⋅b;
среднее гармоническое чиселa и b: 2ab/a+b;
среднее квадратичное чисел a и b: корень a2+b2.

Формат входных данных
На вход программе подается два вещественных числа a и b, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.
"""
from math import sqrt

a, b = float(input()), float(input())

print((a + b) / 2, sqrt(a * b), (2 * a *b) / (a + b), sqrt((a ** 2 + b ** 2)/2), sep='\n')

"""
Второй способ решения
from math import sqrt

a = float(input())
b = float(input())

avg_alg_dgts = (a + b)/2
avg_geom_dgts = sqrt(a * b)
avg_garm_dgts = (2 * a *b) / (a + b)
avg_sqrt_dgts = sqrt((a**2 + b**2)/2)

print(avg_alg_dgts)
print(avg_geom_dgts)
print(avg_garm_dgts)
print(avg_sqrt_dgts)
"""
