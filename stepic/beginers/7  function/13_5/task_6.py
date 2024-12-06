"""Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение
True если указанный текст является палиндромом и False в противном случае.

Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы,
а также символы , . ! ? -.

Примечание 3. Следующий программный код:

print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))
должен выводить:

True
True
False"""


def is_palindrome(text):
    # Удаляем пробелы и знаки препинания, приводим к нижнему регистру
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Проверяем, является ли строка палиндромом
    return cleaned_text == cleaned_text[::-1]


# Считываем данные
txt = input()

# Вызываем функцию
print(is_palindrome(txt))


# Второй способ решения задачи
# объявление функции
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
