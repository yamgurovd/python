"""Первый способ создания матрицы"""
n, m, l = int(input()), int(input()), []

for i in range(n):
    row = []
    for j in range(m):
        el = input()
        row.append(el)
    l.append(row)

print(*l, sep='\n')

"""Второй способ создания матрицы"""
lst = [[i for i in range(n)] for j in range(m)]

print(*lst, sep="\n")

"""Операции с матрицей"""

lst2 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

for i in lst2:
    print(i, sep="\n")
    for j in i:
        print(j, sep="\n")

"""Разбиение матрицы на четверти"""
# Ввод количества строк и столбцов
n = int(input("Введите размер матрицы n: "))
matrix = []

# Считывание элементов матрицы
for i in range(n):
    row = list(map(int, input(f"Введите элементы строки {i + 1} через пробел: ").split()))
    matrix.append(row)

# Инициализация списков для каждой четверти
first_quarter = []
second_quarter = []
third_quarter = []
fourth_quarter = []

# Заполнение списков для каждой четверти
for i in range(n):
    for j in range(n):
        # Первая четверть (верхняя левая)
        if i <= j and i + j < n:
            first_quarter.append(matrix[i][j])

        # Вторая четверть (верхняя правая)
        if i <= j and i + j >= n:
            second_quarter.append(matrix[i][j])

        # Третья четверть (нижняя левая)
        if i >= j and i + j < n:
            third_quarter.append(matrix[i][j])

        # Четвертая четверть (нижняя правая)
        if i >= j and i + j >= n:
            fourth_quarter.append(matrix[i][j])

# Вывод результатов
print("Элементы первой четверти:", first_quarter)
print("Элементы второй четверти:", second_quarter)
print("Элементы третьей четверти:", third_quarter)
print("Элементы четвертой четверти:", fourth_quarter)

# Второй способ разбиения матрицы на четверти
# Ввод количества строк и столбцов
n = int(input("Введите размер матрицы n: "))
matrix = []

# Считывание элементов матрицы
for i in range(n):
    row = list(map(int, input(f"Введите элементы строки {i + 1} через пробел: ").split()))
    matrix.append(row)

# Инициализация сумм для каждой четверти
sum_upper = 0
sum_right = 0
sum_lower = 0
sum_left = 0

# Подсчет сумм для каждой четверти
for i in range(n):
    for j in range(n):
        if i < j and i + j < n:  # Верхняя четверть
            sum_upper += matrix[i][j]
        elif i < j and i + j >= n:  # Правая четверть
            sum_right += matrix[i][j]
        elif i > j and i + j >= n:  # Нижняя четверть
            sum_lower += matrix[i][j]
        elif i > j and i + j < n:  # Левая четверть
            sum_left += matrix[i][j]

# Вывод результатов
print(f"Сумма элементов верхней четверти: {sum_upper}")
print(f"Сумма элементов правой четверти: {sum_right}")
print(f"Сумма элементов нижней четверти: {sum_lower}")
print(f"Сумма элементов левой четверти: {sum_left}")

# Выполнение разных операций над матрицами
# Второй способ решения задачи - взято из форума
m, n = int(input()), int(input())
mult = [[i * j for i in range(n)] for j in range(m)]

for i in range(m):
    for j in range(n):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()

# Еще один способ формирования матрицы
n, m = int(input()), int(input())

mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for row in mult:
    for value in row:
        print(str(value).ljust(3), end=" ")
    print()

# Формирование главной и побочной диагонали
n, mtx = int(input()), []

for i in range(n):
    row = [int(i) for i in input().split()]
    mtx.append(row)

for i in range(n):
    mtx[i][i], mtx[n - i - 1][i] = mtx[n - i - 1][i], mtx[i][i]

for i in range(n):
    print(*mtx[i])

# Формирование матрицы размерностью n на m и вывод строкам
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

# Формирование матрицы размерностью n на m и вывод столбцам
# Считываем количество строк n и столбцов m
n, m = map(int, input().split())

# Инициализируем пустую матрицу
mtx = [[0] * m for _ in range(n)]

# Заполняем матрицу по столбцам
count = 1
for j in range(m):
    for i in range(n):
        mtx[i][j] = count
        count += 1

# Выводим матрицу
for row in mtx:
    print(" ".join(str(el).ljust(2) for el in row))

# ВТорой вариант решения задачи - взято из форума
n, m = map(int, input().split())
matrix = [list(range(i + 1, n * m + 1, n)) for i in range(n)]

[print(*row) for row in matrix]

# Формирование значений измененных по главной и побочной диагонали размерностью nxn
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - 1 - i] = 1

for row in matrix:
    print("".join(str(el).ljust(3) for el in row))

# Формирование матрицы nxm как змейка
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
