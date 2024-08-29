"""
Задание 2.6.6
Напишите программу, которая на вход получает последовательность чисел, а выводит модифицированный список:

Первое и последнее числа последовательности должны поменяться местами.
В конец списка нужно добавить сумму всех чисел.

"""

dig = input("Введите числа через пробел: ").split()

dig_convert = list(map(int, dig))
print(dig_convert)

dig_first = dig_convert[0]
dig_last = dig_convert[-1]
dig_first, dig_last = dig_last, dig_first
dig_sum = sum(dig_convert)
print(dig_sum)

dig_convert.append(dig_sum)
print(dig_convert)

# Предложенный вариант из подсказки
lst = list(map(int, input().split()))

lst[0], lst[-1] = lst[-1], lst[0]

lst.append(sum(lst))
