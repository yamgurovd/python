"""Переставить min и max
На вход программе подается строка текста, содержащая различные натуральные числа. Вам необходимо переставить максимальный и минимальный элементы местами и вывести измененную строку.

Формат входных данных
На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Используйте подходящие встроенные функции и списочные методы."""

lst = list(input().split())

mn = lst.index(min(lst))
mx = lst.index(max(lst))

lst[mn], lst[mx] = lst[mx], lst[mn]

print(*lst)

# Второй способ решения - взято из ГПТ
lst = list(map(int, input().split()))

min_index = lst.index(min(lst))
max_index = lst.index(max(lst))

lst[min_index], lst[max_index] = lst[max_index], lst[min_index]

print(' '.join(map(str, lst)))

# Третий способ решения задачи - взято из форума решений
a = list(map(int, input().split()))
x = a.index(max(a))
y = a.index(min(a))
a[x], a[y] = a[y], a[x]
print(*a)
