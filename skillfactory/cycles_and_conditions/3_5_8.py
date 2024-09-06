"""
Задание 3.5.8

Проверить, все ли элементы в списке являются уникальными.
"""

lst = [1, 3, 4, 56, '2323', "hjkh", 2, 3]

unique_lst = set(lst)

if len(lst) == len(unique_lst):
    print("Yes")
