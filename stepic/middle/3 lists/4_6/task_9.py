"""Заполнение 5 🌶️
На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m, заполнив ее в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение. 😇"""

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

# ВТорой способ решения задачи - взято из форума
n, m = map(int, input().split())
matrix = [[(j + i) % m + 1 for j in range(m)] for i in range(n)]
for item in matrix:
    print(*[str(it).ljust(3) for it in item])
