"""Количество слов
На вход программе подаётся строка текста, состоящая из слов, разделённых ровно одним пробелом. Напишите программу,
которая подсчитывает количество слов в ней.

Формат входных данных
На вход программе подаётся строка текста.

Формат выходных данных
Программа должна вывести количество слов.

Примечание 1. Строка текста не содержит пробелов в начале и конце."""
text = input()

print(text.count(" ") + 1)
