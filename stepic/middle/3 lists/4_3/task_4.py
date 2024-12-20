"""Треугольник Паскаля 2
На вход программе подается натуральное число n.
Напишите программу, которая выводит первые n строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n (n≥1).

Формат выходных данных
Программа должна вывести первые n строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом."""
def pascal(n):
    # Начальная строка треугольника Паскаля
    row = [1]

    for _ in range(n):
        # Создаем новую строку, начиная с 1
        new_row = [1]
        # Заполняем новую строку
        for j in range(1, len(row)):
            new_row.append(row[j - 1] + row[j])
        # Заканчиваем строку 1
        new_row.append(1)
        # Обновляем текущую строку
        row = new_row

    return row


# Ввод числа n
n = int(input("Введите номер строки треугольника Паскаля: "))
# Вывод указанной строки
print(pascal(n))