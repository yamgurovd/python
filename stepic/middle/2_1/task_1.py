"""
На easy
На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:
сумму чисел a и b;
разность чисел a и b;
произведение чисел a и b;
частное чисел a и b;
целую часть от деления числа a на b;
остаток от деления числа a на b;
корень квадратный из суммы их 10-х степеней: корень a10+b10.

Формат входных данных
На вход программе подаются два целых числа a и b(b≠0), каждое на отдельной строке.

подсказка
Целая часть от деления (//)
Остаток от деления (%)
Возведение в степень (**)
Необязательно импортировать библиотеку math для того, чтобы использовать корень (sqrt). Его можно заменить возведением в 0.5 степень (** 0.5)
"""
a, b = int(input()), int(input())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a ** 10 + b ** 10) ** 0.5)


# Решение 2
def get_math(a: int | float,
             b: int | float):
    return print(a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) ** 0.5, sep='\n')


print(get_math(a, b))
# test
