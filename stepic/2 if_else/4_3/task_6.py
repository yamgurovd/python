"""
Самописный калькулятор 🌶️
Напишите программу, которая считывает с клавиатуры два целых числа и строку.
Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /),
то выведите результат применения этой операции к введённым ранее числам,
в противном случае выведите «Неверная операция» (без кавычек). Если пользователь захочет поделить на ноль,
выведите текст «На ноль делить нельзя!» (без кавычек).

Формат входных данных
На вход программе подаются два целых числа и строка, все на отдельной строке.

Формат выходных данных
Программа должна вывести результат применения операции к введенным числам или соответствующий текст,
если операция неверная либо если происходит деление на ноль.
"""

dig_1 = int(input())
dig_2 = int(input())
action = input()

if action == '+':
    print(dig_1 + dig_2)
elif action == '-':
    print(dig_1 - dig_2)
elif action == '*':
    print(dig_1 * dig_2)
elif action == '/':
    if dig_2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(dig_1 / dig_2)
else:
    print("Неверная операция")