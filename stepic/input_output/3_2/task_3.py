"""
Как известно, целые числа в языке Python не имеют ограничений, которые встречаются в других языках программирования.
Напишите программу, которая считывает четыре целых положительных числа
a,b,c и d и выводит на экран значение выражения ab+cd.
Формат входных данных
На вход программе подаются четыре целых положительных числа
a,b,c и d, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести значение
a**b+c**d.
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a ** b + c ** d)
