"""
Роскомнадзор 🔞
Напишите программу, которая определяет, разрешён ли пользователю доступ к интернет-ресурсу или нет.

Формат входных данных
На вход программе подаётся целое число – возраст пользователя.

Формат выходных данных
Программа должна вывести текст «Доступ разрешен», если возраст пользователя не менее 18 лет, или «Доступ запрещен» в противном случае.
"""

age = int(input())

if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
