"""
Только + 🌶️
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

Формат входных данных
На вход программе подаются три целых числа, каждое на новой строке.

Формат выходных данных
Программа должна вывести одно число – сумму положительных чисел.

Примечание. Если положительных чисел нет, то следует вывести 0.
"""

a = int(input())
b = int(input())
c = int(input())
sum_ = 0

if a >= 0:
    sum_ += a
if b >= 0:
    sum_ += b
if c >= 0:
    sum_ += c
    print(sum_)
else:
    print(sum_)

if sum_ < 0:
    print(0)