"""
Разделяй и властвуй
Напишите программу, которая считывает целое положительное число
x и выводит на экран последовательность чисел
x,2x,3x,4x и 5x, разделённых тремя черточками.

Формат входных данных
На вход программе подаётся целое положительное число.

Формат выходных данных
Программа должна вывести текст согласно условию задачи.
"""

x = int(input())
print(x, 2*x, 3*x, 4*x, 5*x, sep='---')