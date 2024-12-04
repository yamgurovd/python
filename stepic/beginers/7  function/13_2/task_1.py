"""Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число."""


# объявление функции
def draw_triangle(fill, base):
    for i in range(1, (base) // 2 + 1):
        for j in range(i):
            print(fill, end='')
        print()

    for i in range((base) // 2 + 1, 0, -1):
        for j in range(i):
            print(fill, end='')
        print()


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)


# Второй способ решения задачи - взято из форума
# объявление функции
def draw_triangle(fill, base):
    for i in range(base // 2):
        print(fill * (i + 1))

    for i in range(base // 2, -1, -1):
        print(fill * (i + 1))


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)


# Третий способ решения задачи - взято из форума
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)
    for i in range(base // 2, 0, -1):
        print(fill * i)


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
