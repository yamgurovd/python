"""Найти всех
Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке.
Проблема заключается в том, что данный метод не находит местоположение всех символов а.

Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и
возвращает список, содержащий все местоположения этого символа в строке.

Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

Примечание 2. Следующий программный код:

print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))
должен выводить:

[0, 4, 7, 8, 9]
[]
[4]"""


# объявление функции
def find_all(target, symbol):
    cur = 0
    res = []

    for i in target:
        if i == symbol:
            res.append(cur)

        cur += 1

    return res


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
print(find_all(s, char))


# Второй способ решения задачи - взято из форума
# объявление функции
def find_all(target, symbol):
    return [x for x in range(len(target)) if target[x] == symbol]


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))


# Третий способ решения задачи - взято от Гигачата
# объявление функции
def find_all(target, symbol):
    positions = []
    start = 0
    while True:
        pos = target.find(symbol, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions


# считываем данные
s = input()
char = input()

# вызываем функцию
result = find_all(s, char)
print(result)
