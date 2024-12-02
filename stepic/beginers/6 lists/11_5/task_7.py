"""Количество совпадающих пар
На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел.
Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

Формат входных данных
На вход программе подается строка текста, содержащая целые числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести одно число – количество пар элементов, равных друг другу."""
text = list(input().split())
count = 0

for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] == text[j]:
            count += 1
print(count)
