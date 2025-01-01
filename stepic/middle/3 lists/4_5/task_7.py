"""Поворот матрицы 🔁
Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом."""

n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

# Инициализация новой матрицы для результата
rotated_matrix = [[0] * n for _ in range(n)]

# Поворот матрицы на 90 градусов по часовой стрелке
for i in range(n):
    for j in range(n):
        rotated_matrix[j][n - 1 - i] = matrix[i][j]

# Вывод результата
for row in rotated_matrix:
    print(' '.join(map(str, row)))

# Второй способ решения задачи - взято из форума
n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n)[::-1]:
        print(array[j][i], end=' ')
    print()


