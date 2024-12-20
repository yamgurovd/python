"""
Площадь и длина
Напишите программу, определяющую площадь круга и длину окружности по заданному радиусу R.

Формат входных данных
На вход программе подаётся одно действительное число R.

Формат выходных данных
Программа должна вывести два числа (каждое на новой строке) – площадь круга и длину окружности радиуса R.

Примечание. Используйте константу math.pi.
"""
from math import pi

r = float(input())

s = pi*r**2
c = 2*pi*r
print(s, c, sep="\n")


"""
import math
r = float(input())

s = math.pi * r**2
c = 2 * math.pi * r

print(s)
print(c)
"""