"""Две половинки
На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части,
переставит их местами и выведет на экран.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если длина строки нечетная, то длина первой части должна быть на один символ больше."""
# Вводим строку
s = input()

# Определяем длину строки
length = len(s)

# Вычисляем середину строки
mid = length // 2

# Разделяем строку на две половины
first_half = s[:mid + (length % 2)]
second_half = s[mid + (length % 2):]

# Меняем половины местами и выводим результат
print(second_half + first_half)