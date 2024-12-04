"""Звездный прямоугольник 1
Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:

**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
Примечание. Для вывода прямоугольника используйте цикл for.  """


# объявление функции
def draw_box():
    for i in range(14):
        print("*" * 10)

        if i == 1:
            break
        for j in range(8):
            print("*        *")


# основная программа
draw_box()  # вызов функции

# Второй способ решения задачи - взято из форума решений
# объявление функции
def draw_box():
    print("*" * 10)

    for i in range(12):
        print("*", "*", sep=" " * 8)

    print("*" * 10)


# основная программа
draw_box()  # вызов функции