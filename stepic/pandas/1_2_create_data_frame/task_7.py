"""Упражнение 7.
Создайте DataFrame содержащий 3 столбца и 3 строки.

Результат запишите в переменную df."""
import pandas as pd

dict_in = {
    "row_1": [1, "test 123", 11.99],
    "row_2": [2, "test 124", 22.00],
    "row_3": [3, "test 125", 33.11]
}
df = pd.DataFrame(data=dict_in)
print(df)


# Решение от Гигачат
import pandas as pd

# Создаем словарь с данными
data = {
    'column_1': [1, 2, 3],
    'column_2': ['test 123', 'test 124', 'test 125'],
    'column_3': [11.99, 22.00, 33.11]
}

# Создаем DataFrame из словаря
df = pd.DataFrame(data)

# Выводим DataFrame
print(df)