"""Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
и возвращает значение True, если пароль является надёжным, или False в противном случае.

Пароль является надёжным, если:

его длина не менее 8 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
Примечание. Следующий программный код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
должен выводить:

True
False"""


# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False

    flag1 = False
    flag2 = False
    flag3 = False

    for i in password:
        if i.isupper():
            flag1 = True
        elif i.islower():
            flag2 = True
        elif i.isdigit():
            flag3 = True

    return flag1 and flag2 and flag3


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))


# Второй способ решения задачи
def is_password_good(password):
    f1, f2, f3 = 0, 0, 0
    for i in password:
        if '0' <= i <= '9':
            f1 = 1
        elif 'a' <= i <= 'z':
            f2 = 1
        elif 'A' <= i <= 'Z':
            f3 = 1
    if f1 and f2 and f3 and len(password) > 7:
        return True
    return False


txt = input()
print(is_password_good(txt))
