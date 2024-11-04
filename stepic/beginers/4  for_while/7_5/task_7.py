"""Упорядоченные цифры 🌶️
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре
справа налево упорядоченной по неубыванию.

Формат входных данных
На вход программе подаётся одно натуральное число.

Формат выходных данных
Программа должна вывести «YES», если последовательность его цифр при просмотре справа налево является упорядоченной
по неубыванию, или «NO» в противном случае."""

list = []
num = int(input())
saven = num
mybool = True
while saven > 0:
    list.append(saven % 10)
    saven //= 10

if num > 9:
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            mybool = False

if mybool:
    print('YES')
else:
    print('NO')


# Второй способ решения
n = int(input())
flag = True
last_digit = n % 10

while n > 0:
    if last_digit > n % 10:
        flag = False

    last_digit = n % 10
    n //= 10

if flag:
    print("YES")
else:
    print("NO")