"""
Задание 3.3.1
Напишите выражение (задание на самопроверку).

Дано n-значное целое число N. Определить: входят ли в него цифры 3 и 7.
"""

N = list(map(int, list(input("Введите число").split())))

if 3 and 7 in N:
    print("YES")
else:
    print("NO")

# Пример решения из подсказки задания
print('3' in str(N) and '7' in str(N))
