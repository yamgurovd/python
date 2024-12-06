"""Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True,
если число является простым, или False в противном случае.

 Примечание. Следующий программный код:

print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
должен выводить:

False
False
True"""


# объявление функции
def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))


# Второй способ решения задачи - взято из форума
# объявление функции
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True if num != 1 else False


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
