"""
Задание 3.5.1 (External resource)
Запишите вместо вопросительных знаков выражение, которое вернет True, когда каждое из чисел А и В нечетное.
"""


def are_both_odd(a: int, b: int) -> bool:
    return a % 2 != 0 and b % 2 != 0
