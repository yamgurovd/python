"""Упражнение 13.

В программе создан DataFrame и записан в переменную df. Столбцы ['client', 'product']
запишите в файл 'data.csv'. Файл 'data.csv' не должен содержать индексы строк df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована."""
import pandas as pd

df = pd.read_csv(
    filepath_or_buffer="data_11.csv",
    sep=","
)

print(df)

df.to_csv(path_or_buf="data_11_download.csv",
          index=False,
          columns=["client", "product"])
