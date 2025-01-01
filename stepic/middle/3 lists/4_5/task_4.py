"""Симметричная матрица 💠
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, или NO в противном случае.
"""
n, mtx = int(input()), []

for i in range(n):
    row = [int(i) for i in input().split()]
    mtx.append(row)

print(*mtx, sep='\n')

is_symmetric = True

for i in range(n):
    for j in range(n):

        if mtx[[i][j]] != mtx[j][i]:
            is_symmetric = False
            break

        if not is_symmetric:
            break

if is_symmetric:
    print('YES')
else:
    print('NO')

# Второй способ решения задачи - взято из форума
n = int(input())
matrix = [input().split() for _ in range(n)]
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)

# Третий способ решения задачи - взято из форума
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
if all([matrix[i][j] == matrix[j][i] for j in range(n) for i in range(n)]):
    print('YES')
else:
    print('NO')
