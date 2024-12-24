"""Таблица умножения
На вход программе подаются два натуральных числа n и m – количество строк и столбцов в матрице.
Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа n и m – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа
(для этого используйте строковый метод ljust())."""

n, m = int(input()), int(input())

mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for row in mult:
    for value in row:
        print(str(value).ljust(3), end=" ")
    print()


# Второй способ решения задачи - взято из форума
m, n = int(input()), int(input())
mult =[[i*j for i in range(n)] for j in range(m)]

for i in range(m):
    for j in range(n):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()