"""Магический квадрат ✨🌶️
Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3, …, n2 так,
что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы:
n строк, по n чисел в каждой, разделенные пробелами.

Формат выходных данных
Программа должна вывести YES, если матрица является магическим квадратом, или NO в противном случае."""


def sum_matrix(n, total, matrix):
    total += sum(matrix[i][j] for j in range(n) for i in range(n))  # сумма строк
    total += sum(matrix[j][i] for j in range(n) for i in range(n))  # сумма столбцов
    total += sum(matrix[i][i] for i in range(n))  # сумма главной диагонали
    total += sum(matrix[i][n - i - 1] for i in range(n))  # сумма второстепенной диагонали
    return total


n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
total = 0
total = sum_matrix(n, total, matrix) / (n + n + 2)  # сумма матрицы деленная на количество столбцов, строк и диаг
flag = False
l = [matrix[i][j] for j in range(n) for i in range(n)]
l.sort()
if l == [i for i in range(1, n ** 2 + 1)]:
    flag = True
print('YES' if total == sum(matrix[-1]) and flag == True else 'NO')

""""Второй способ решения задачи - взято из Perplexity"""

# Ввод количества строк и столбцов
n = int(input())

# Считывание элементов матрицы
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Проверка наличия всех чисел от 1 до n^2
expected_numbers = set(range(1, n * n + 1))
actual_numbers = set()

for row in matrix:
    actual_numbers.update(row)

if actual_numbers != expected_numbers:
    print("NO")
    exit()

# Сумма для сравнения
magic_sum = sum(matrix[0])  # Сумма первой строки

# Проверка сумм строк
for i in range(n):
    if sum(matrix[i]) != magic_sum:
        print("NO")
        exit()

# Проверка сумм столбцов
for j in range(n):
    if sum(matrix[i][j] for i in range(n)) != magic_sum:
        print("NO")
        exit()

# Проверка главной диагонали
if sum(matrix[i][i] for i in range(n)) != magic_sum:
    print("NO")
    exit()

# Проверка побочной диагонали
if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:
    print("NO")
    exit()

# Если все проверки пройдены
print("YES")
