"""Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке."""

num = int(input())
sum_ = 0
counter = 0
multipal = 1
middle = sum_ / counter

while num != 0:
    last_digit = num % 10
    sum_ += last_digit
    counter += 1
    multipal *= last_digit

# Второй способ решения
# put your python code here
list = []
num = int(input())
while num > 0:
    list.append(num % 10)
    num //= 10

sum = 0
mult = 1
for i in list:
    sum = sum + i
    mult = mult * i

print(sum)
print(len(list))
print(mult)
print(sum / len(list))
print(list[len(list) - 1])
print(list[len(list) - 1] + list[0])
