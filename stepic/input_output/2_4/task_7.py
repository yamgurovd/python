"""
Арифметические операции
Напишите программу, которая принимает на вход два числа
a и b, вычисляет сумму, разность и произведение для этих чисел и выводит текст в следующем формате:

<число a> + <число b> = <сумма чисел a и b>
<число a> - <число b> = <разность чисел a и b>
<число a> * <число b> = <произведение чисел a и b>
Формат входных данных
На вход программе подаются два целых числа (каждое на отдельной строке):
a и b.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""

a = int(input())
b = int(input())

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
