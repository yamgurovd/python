"""Заполнение змейкой 🐍
На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m, заполнив ее "змейкой" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение. 😇"""

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

num = 1

for i in range(n):

    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = num
            num += 1
    else:
        for j in range(m - 1, -1, -1):
            matrix[i][j] = num
            num += 1

for row in matrix:
    print("".join(str(el).ljust(3) for el in row))

# Второй способ решения задачи - взято из форума
n, m = map(int, input().split())
d = 1
row = [[str(j).ljust(3) for j in range(1 + m * i, m + 1 + m * i)] for i in range(n)]
for i in range(n):
    if i % 2 != 0:
        row[i].reverse()
    print(*row[i])
