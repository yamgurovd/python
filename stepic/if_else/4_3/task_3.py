"""
Серединное число
Даны три различных целых числа. Напишите программу, которая находит серединное значение из этих чисел.

Формат входных данных
На вход программе подаются три различных целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести серединное значение из набора трёх чисел.

Примечание. Серединное значение набора чисел — число, которое находится в середине этого набора,
если его упорядочить по возрастанию.

link - https://stepik.org/lesson/265082/step/5?auth=registration&unit=246030

подсказка из комментария - если x > y и z > x или z > x и y > x : выводим (х) и тоже делаем для y и z.
"""

dig_1: int = int(input("Введите целое число 1: "))
dig_2: int = int(input("Введите целое число 2: "))
dig_3: int = int(input("Введите целое число 3: "))

if dig_1 > dig_2 and dig_3 > dig_1 or dig_3 > dig_1 and dig_2 < dig_1:
    print(dig_1)
elif dig_2 > dig_1 and dig_3 > dig_2 and dig_3 > dig_2 and dig_1 < dig_2:
    print(dig_2)
elif dig_3 > dig_1 and dig_2 > dig_3 or dig_1 > dig_3 and dig_2 < dig_3:
    print(dig_3)
# Пример решения с гигачат

# Проверка на равенство
if dig_1 == dig_2 or dig_2 == dig_3 or dig_3 == dig_1:
    print("Одно из чисел равны друг другу")
    exit()

# Нахождение наименьшего числа
smallest = dig_1
if dig_2 < smallest:
    smallest = dig_2
if dig_3 < smallest:
    smallest = dig_3

# Нахождение срединного числа
mid_candidate = smallest + 1
if mid_candidate == dig_2:
    if dig_3 > dig_1:
        mid_candidate = dig_1
    else:
        mid_candidate = dig_3
else:
    if mid_candidate == dig_3:
        mid_candidate = dig_2
    elif mid_candidate == dig_1:
        mid_candidate = dig_2

print(mid_candidate)
