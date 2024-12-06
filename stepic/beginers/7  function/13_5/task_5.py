"""Ровно в одном 1️⃣
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
возвращает значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе,
или значение False в противном случае.

 Примечание. Следующий программный код:

print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
должен выводить:

True
True
False
False"""
from itertools import count


# объявление функции
def is_one_away(word1, word2):
    counter = 0
    if len(word1) == len(word2):
        return True
        for i in range(len(word1)):

            if word1[i] == word2[i]:
                counter += 1
        if counter + 1 == len(word1):
            return True

    return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))


# Второй способ решения задачи - взято из Гигачата
# Объявляем функцию
def is_one_away(word1, word2):
    # Проверяем, равны ли длины слов
    if len(word1) != len(word2):
        return False

    # Счетчик для количества различающихся символов
    difference_count = 0

    # Проходим по каждому символу в словах
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            difference_count += 1

        # Если разница уже больше одного символа, прерываем цикл
        if difference_count > 1:
            break

    # Возвращаем True, если разница ровно в одном символе, иначе False
    return difference_count == 1


# Считываем данные
txt1 = input()
txt2 = input()

# Вызываем функцию
print(is_one_away(txt1, txt2))


# Третий способ решения задачи - взято из форума
# объявление функции
def is_one_away(word1, word2):
    counter = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1
    return counter == 1


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
