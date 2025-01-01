"""Обмен столбцов ⏸️
Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа n и m – количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел, затем натуральные числа i и j – номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами."""
# Ввод количества строк и столбцов
n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))

# Инициализация матрицы
mtx = []

# Заполнение матрицы
start_value = 11  # Начальное значение
for i in range(n):
    row = []  # Создаем новую строку
    for j in range(m):
        row.append(start_value)  # Добавляем текущее значение в строку
        start_value += 1  # Увеличиваем значение для следующей ячейки
    mtx.append(row)  # Добавляем заполненную строку в матрицу

# Вывод матрицы
print(*mtx, sep='\n')

# Второй способ решения задачи - взято из форума
n, m = int(input()), int(input())
l = [list(map(int, input().split())) for i in range(n)]
print(*l, sep='\n')
i, j = (map(int, input().split()))
print(i, j)
for k in l:
    k[i], k[j] = k[j], k[i]
    print(*k)

n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
res = [int(i) for i in input().split()]
for i in range(n):
    matrix[i][res[0]], matrix[i][res[1]] = matrix[i][res[1]], matrix[i][res[0]]
    print(*matrix[i])