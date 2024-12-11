"""Орел и решка
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" соответствует выпадению Орла,
а буква "Р" - выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 0"""
# Чтение входной строки
sequence = input()

# Инициализация переменных для хранения длины текущей последовательности и максимальной длины
current_sequence_length = 0
max_sequence_length = 0

# Прохождение по символам строки
for char in sequence:
    if char == 'Р':
        current_sequence_length += 1
        max_sequence_length = max(max_sequence_length, current_sequence_length)
    else:
        current_sequence_length = 0

# Вывод максимального количества подряд выпавших Решек
print(max_sequence_length)

# Второй способ решения задачи - взято из форума решений
s = input()
seq = s.split("О")  # убираем всех орлов и группируем решек

mx = 0  # максимум подряд идущих решек
for el in seq:
    mx = max(mx, el.count("Р"))

print(mx)
