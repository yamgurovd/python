"""
Квадрат суммы 🆚 Сумма квадратов
Напишите программу, которая считывает два целых числа
a и b и выводит на экран квадрат суммы (a+b)2 и сумму квадратов a2+b2 этих чисел в следующем формате:

Квадрат суммы <a> и <b> равен <квадрат суммы a и b>
Сумма квадратов <a> и <b> равна <сумма квадратов a и b>
"""

a = int(input())
b = int(input())

print(f"Квадрат суммы {a} и {b} равен {(a + b) ** 2}", f"Сумма квадратов {a} и {b} равна {a ** 2 + b ** 2}", sep="\n")
