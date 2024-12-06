"""Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает
первое простое число, большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

 Примечание 2. Следующий программный код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
должен выводить:

7
11
17"""


# объявление функции
def get_next_prime(num):
    num += 1

    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))


# ВТорой способ решения задачи
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_next_prime(num):
    m = num + 1
    while is_prime(m) == False:
        m += 1
    return m


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
