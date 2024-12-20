"""Делители-2
На вход программе подается натуральное числоn.
Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно.
В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести графическое изображение чисел от 1 до n, каждое на отдельной строке.

# Считываем число и записываем в переменную 'n'
# Создаем внешний цикл 'i' от 1 до 'n' включительно
# Создаем внутри цикла счетчик обнулятор counter равный 0
# Создадим внутренний цикл 'j' от 1 до 'i' включительно
# Внутри создаем условие если 'i' % 'j' равно 0
# Счетчик + 1
# Теперь правильно выводим ответ на равне с внутренним циклом
(i, соединяем end)((а можно и sep тогда второй принт необязателен))
# На равне с ответом принт с '+' * counter разбиваем по строкам"""
n = int(input())

for i in range(1, n + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    print(i, end="")
    print("+" * counter)
