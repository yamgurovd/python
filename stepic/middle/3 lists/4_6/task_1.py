"""Шахматная доска
На вход программе подаются два натуральных числа n и m.
Напишите программу для создания матрицы размером n×m, заполнив ее символами . и * в шахматном порядке.
В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке через пробел подаются два натуральных числа n и m – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи."""
m, n = map(int, input().split())

matrix = []

for i in range(n):
    row = []

    for j in range(m):
        if (i + j) % 2 == 0:
            row.append('.')
        else:
            row.append('*')

    matrix.append(row)

for row in matrix:
    print(" ".join(row))