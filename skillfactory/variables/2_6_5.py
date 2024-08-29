"""
Область применения функции очень большая, но мы остановимся на одном её применении — ввод данных.
Вспомним, что даже при вводе чисел во время выполнения функции input(), они все равно остаются в строковом представлении.
Если ввести сразу несколько чисел через пробел, то тем более они останутся в таком виде.

Однако, пользуясь функциями split() и map(), можно выполнить нужное преобразование:

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел

print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка
"""

dig_txt = input("Введите числа через пробел: ")
dig_convert = dig_txt.split()
print(dig_convert)
dig_after_convert = list(map(int, dig_convert))
print(dig_after_convert)
print(sum(dig_after_convert))