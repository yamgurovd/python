"""Инициалы
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.

Формат входных данных
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""
fio = list(input().split())

for i in fio:
    print(f"{i[0]}.", end=" ")

# Второй способ решения
text = input().split()

for i in range(len(text)):
    print(text[i][0], end='.')