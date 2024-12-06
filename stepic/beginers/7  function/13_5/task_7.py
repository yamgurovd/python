"""BEEGEEK 🐝
BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое з
начение пароля password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка,
или False в противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
должен выводить:

True
False
False
False"""


# объявление функции
def is_valid_password(password):
    lst = [str(i) for i in password.split(':')]
    print(lst)

    flag1 = False
    flag2 = False
    flag3 = False

    if len(lst) == 3:
        a = str(lst[0])
        b = int(lst[1])
        c = int(lst[2])

        if a == a[::-1]:
            flag1 = True

        for i in range(2, b):
            if b % i == 0:
                flag2 = True

        if c % 2 == 0:
            flag3 = True

        if flag1 and flag2 and flag3:
            return True

    return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))


# Третий способ решения задачи - взято из форума
def is_valid_password(password):
    password = password.split(':')
    a, b, c = password[0], int(password[1]), int(password[2])
    if len(password) != 3 or a != a[::-1] or c % 2 != 0:
        return False
    for i in range(2, b):
        if b % i == 0:
            return False
    return True


psw = input()
print(is_valid_password(psw))


# Третий способ решения задачи - взято из Гигачата
def is_prime(num):
    """Функция для проверки, является ли число простым."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_even(num):
    """Функция для проверки, является ли число чётным."""
    return num % 2 == 0


def is_palindrome(string):
    """Функция для проверки, является ли строка палиндромом."""
    return string == string[::-1]


def is_valid_password(password):
    parts = password.split(":")

    if len(parts) != 3:
        return False

    a, b, c = parts

    try:
        b = int(b)
        c = int(c)
    except ValueError:
        return False

    return (
            is_palindrome(a) and
            is_prime(b) and
            is_even(c)
    )


# Считываем данные
psw = input()

# Вызываем функцию
print(is_valid_password(psw))
