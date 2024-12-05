"""Merge lists 1
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка,
состоящих из целых чисел, и объединяет их в один отсортированный список.

Примечание 1. Списки list1 и list2 могут иметь разную длину.

Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него. 😎

Примечание 3. Следующий программный код:

print(merge([1, 2, 3], [5, 6, 7, 8]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
должен выводить:

[1, 2, 3, 5, 6, 7, 8]
[1, 5, 6, 7, 10, 13, 16, 20]"""


# объявление функции
def merge(list1, list2):
    result = (list1 + list2)
    print(result.sort(list1))

    return result


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))


def merge(list1, list2):
    # Объединяем списки
    merged_list = list1 + list2
    # Сортируем объединённый список
    merged_list.sort()
    return merged_list


# Считывание данных
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# Вызов функции
merged_result = merge(numbers1, numbers2)
print(merged_result)


# Второй способ решения задачи - взято из форума
def merge(list1, list2):
    return sorted(list1 + list2)


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
print(merge(numbers1, numbers2))
