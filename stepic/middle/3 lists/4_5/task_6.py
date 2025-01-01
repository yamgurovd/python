"""Зеркальное отображение 🦋
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно
горизонтальной оси симметрии.

Формат входных данных
На вход программе подается натуральное числоn – количество строк и столбцов в матрице, з
атем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести матрицу, в которой зеркально отображены элементы относительно горизонтальной оси симметрии."""

n, mtx, mtx_reversed = int(input()), [], []

for i in range(n):
    row = list(map(int, input().split()))
    mtx.append(row)

mtx_reversed = mtx[::-1]

for i in range(n):
    print(*mtx_reversed[i])

# Второй способ решения задачи - взято из форума
n = int(input())

matrix = [[int(item) for item in input().split()] for _ in range(n)]
matrix.reverse()

for row in matrix:
    print(*row)
