"""Вывести матрицу 1
На вход программе подаются два натуральных числа n и m,
каждое на отдельной строке – количество строк и столбцов в матрице. Далее вводятся сами элементы матрицы – слова,
каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и так далее.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

Формат входных данных
На вход программе подаются два числа n и m – количество строк и столбцов в матрице,
далее идут n×m слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом."""

n, m, lst = int(input()), int(input()), []

for i in range(n):
    row = []

    for j in range(m):
        element = input()

        row.append(element)
        lst.append(row)

print(*lst, sep='\n')

# Второй способ решения задачи - взято из Perplxity
# Ввод количества строк и столбцов
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

# Инициализация матрицы
matrix = []

# Считывание элементов матрицы
for i in range(n):
    row = []
    for j in range(m):
        element = input(f"Введите элемент [{i + 1}, {j + 1}]: ")
        row.append(element)
    matrix.append(row)

# Вывод матрицы
for row in matrix:
    print(' '.join(row))

# Третий способ решения задачи
n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# Четвертый способ решения задачи - взято из форума решений
n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)
