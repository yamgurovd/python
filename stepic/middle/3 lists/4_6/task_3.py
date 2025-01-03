"""Заполнение 1
На вход программе подаются два натуральных числа n и m. Напишите программу,
которая создает матрицу размером n×m и заполняет ее числами от 1 до n⋅m в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение. 😇"""
# Ввод натуральных чисел n и m
n, m = map(int, input().split())

# Создание матрицы размером n x m
matrix = []

# Заполнение матрицы числами от 1 до n*m
count = 1
for i in range(n):
    row = []
    for j in range(m):
        row.append(count)
        count += 1
    matrix.append(row)

# Вывод матрицы с форматированием
for row in matrix:
    print("".join(str(el).ljust(3) for el in row))

# Второй способ решения задачи - взято из форума
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

# Третий способ решения задачи - взято из форума
n, m = [int(i) for i in input().split()]
matrix = [list(range(m * i + 1, m * i + 1 + m)) for i in range(n)]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
