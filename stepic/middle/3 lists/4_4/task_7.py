"""Суммы четвертей
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю,
нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Элементы диагоналей не учитываются.
"""

# Ввод количества строк и столбцов
n = int(input())
matrix = []

# Считывание элементов матрицы
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Инициализация сумм для каждой четверти
sum_upper = 0
sum_right = 0
sum_lower = 0
sum_left = 0

# Подсчет сумм для каждой четверти
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:  # Верхняя четверть
            sum_upper += matrix[i][j]
        elif i < j and i > n - 1 - j:  # Правая четверть
            sum_right += matrix[i][j]
        elif i > j and i > n - 1 - j:  # Нижняя четверть
            sum_lower += matrix[i][j]
        elif i > j and i < n - 1 - j:  # Левая четверть
            sum_left += matrix[i][j]

# Вывод результатов
print(f"Верхняя четверть: {sum_upper}")
print(f"Правая четверть: {sum_right}")
print(f"Нижняя четверть: {sum_lower}")
print(f"Левая четверть: {sum_left}")

# ВТорой способ решения задачи - взято из форума
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
upper, lower, left, right = 0, 0, 0, 0

for i in range(n):
    upper += sum(matrix[i][i + 1:n - i - 1])
    left += sum(matrix[i][:min(i, n - i - 1)])
    right += sum(matrix[i][max(n - i, i + 1):])
    lower += sum(matrix[i][n - i:i])

print(f'Верхняя четверть: {upper}')
print(f'Правая четверть: {right}')
print(f'Нижняя четверть: {lower}')
print(f'Левая четверть: {left}')

# Третий способ решения задачи - взято из форума
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
upper, lower, left, right = 0, 0, 0, 0

for i in range(n):
    upper += sum(matrix[i][i + 1:n - i - 1])
    left += sum(matrix[i][:min(i, n - i - 1)])
    right += sum(matrix[i][max(n - i, i + 1):])
    lower += sum(matrix[i][n - i:i])

print(f'Верхняя четверть: {upper}')
print(f'Правая четверть: {right}')
print(f'Нижняя четверть: {lower}')
print(f'Левая четверть: {left}')
