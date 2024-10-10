"""
Геометрической прогрессией называется последовательность чисел b1,b2,…,bn, каждое из которых, начиная с b2
получается из предыдущего умножением на одно и то же постоянное число q(знаменатель прогрессии).
Если известен первый член прогрессии и ее знаменатель, то n-ый член геометрической прогрессии находится по формуле
bn=b1⋅q n−1
Входные данные
На вход программе подаются три целых числа:
b1 q и n каждое на отдельной строке.

Выходные данные
Программа должна вывести n-ый член геометрической прогрессии.
"""

b1 = int(input())
q = int(input())
n = int(input())

bn = b1 * q ** (n - 1)
print(bn)
