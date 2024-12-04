"""Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумму его цифр."""


# объявление функции
def print_digit_sum(num):
    cnt = 0

    while num > 0:
        cnt += num % 10
        num //= 10

    print(cnt)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)


# Второй способ решения задачи - взято из форума
def print_digit_sum(num):
    print(sum([int(i) for i in num]))


print_digit_sum(input())
