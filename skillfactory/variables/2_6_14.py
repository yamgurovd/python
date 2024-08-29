"""
Чтобы не ходить далеко за примером, вернёмся к базе абонентов мобильного оператора. Пусть у нас есть множество
абонентов (для простоты — фамилии) и множество должников, а мы хотим получить множество абонентов, не имеющих долгов.
"""

abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов"}

non_debtors_1 = abons.difference(debtors)
non_debtors_2 = debtors.union(debtors)
non_debtors_3 = abons.symmetric_difference(debtors)
non_debtors_4 = debtors.intersection(debtors)
print(non_debtors_1)
print(non_debtors_2)
print(non_debtors_3)
print(non_debtors_4)


"""
Найдите ошибку в коде, исправьте и укажите в поле ответа скорректированную строку полностью. 
Представленная ниже программа должна находить множество символов, которые встречаются в двух строках одновременно.

"""

text_1 = set(input("Введите текст: "))
text_2 = set(input("Введите текст: "))

text_2.intersection(text_1)
print(text_2)
text_2.union(text_1)
print(text_2)
text_1.difference_update(text_2)
print(text_1)
