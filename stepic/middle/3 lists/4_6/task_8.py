"""    Заполнение 4
На вход программе подается натуральное число n.
Напишите программу, которая создает матрицу размером n×n, заполнив ее в соответствии с образцом.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение. 😇
"""
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):

        if (i-j <=1) and (j - i <= 1):
            matrix[i][j] = 1

for row in matrix:
    print("".join(str(el).ljust(3) for el in row))
