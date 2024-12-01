"""Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers."""
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

sum_of_squares = sum(x * x for x in numbers)

print(sum_of_squares)

# Второй способ решения задачи - взято из форума
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

square_numbers = []
for el in numbers:
    square_numbers.append(el ** 2)

print(sum(square_numbers))
