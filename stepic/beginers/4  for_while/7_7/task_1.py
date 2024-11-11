"""Ревью кода-1 🌶️🌶️
На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке). Нужно написать программу,
которая выводит на экран количество неотрицательных чисел последовательности и их произведение.
Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может
быть исправлена без изменения других строк.

Примечание. При необходимости вы можете добавить необходимые строки кода."""

counter = 0
multi = 1
for i in range(10):
    num = int(input("Enter a number: "))
    if num > 0:
        counter += 1
        multi *= num

if counter > 0:
    print(counter)
    print(multi)
else:
    print('NO')