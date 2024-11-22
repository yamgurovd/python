"""Упражнение 5.

dict_in = {'col_1': [1, 2, 3, 4, 5],
           'col_2': [1, 2, 3, 4, 5],
           'col_3': [1, 2, 3, 4, 5]}
 На основе данного словаря создайте DataFrame и запишите его в переменную df. После чего поменяйте индексы строк
 на row_1, row_2, row_3, row_4, row_5."""
import pandas as pd

dict_in = {'col_1': [1, 2, 3, 4, 5],
           'col_2': [1, 2, 3, 4, 5],
           'col_3': [1, 2, 3, 4, 5]}

rows = ["row_1", "row_2", "row_3", "row_4", "row_5"]

df = pd.DataFrame(
    data=dict_in,
    index=rows
)
print(df)


# Второй вариант решения
import pandas as pd

# Исходный словарь
dict_in = {
    'col_1': [1, 2, 3, 4, 5],
    'col_2': [1, 2, 3, 4, 5],
    'col_3': [1, 2, 3, 4, 5]
}

# Создаем DataFrame на основе словаря
df = pd.DataFrame(dict_in)

# Определяем новые индексы
new_index = ['row_' + str(i+1) for i in range(len(df))]

# Меняем индексы строк
df.index = new_index

# Выводим результат
print(df)
