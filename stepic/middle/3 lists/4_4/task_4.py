"""Больше среднего
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
больших среднего арифметического элементов данной строки.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести n чисел – для каждой строки количество элементов матрицы,
больших среднего арифметического элементов данной строки."""

# Ввод количества строк и столбцов
n = int(input())

# Инициализация матрицы
matrix = []

# Считывание элементов матрицы
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Список для хранения результатов
results = []

# Обработка каждой строки
for row in matrix:
    average = sum(row) / len(row)  # Вычисляем среднее арифметическое
    count_greater_than_average = sum(1 for x in row if x > average)  # Подсчитываем элементы больше среднего
    results.append(count_greater_than_average)

# Вывод результата
for result in results:
    print(result)

# Второй способ решения задачи - взято из форума
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    counter = 0
    average = sum(matrix[i]) / n
    for j in range(n):
        if matrix[i][j] > average:
            counter += 1
    print(counter)

# Третий способ решения задачи - взято из форума
for _ in range(int(input())):
    lst = list(map(int, input().split()))
    avg = sum(lst) / len(lst)
    print(sum(i > avg for i in lst))
