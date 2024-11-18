"""Упражнение 12.

В программе создан DataFrame и записан в переменную df. Столбцы ['client', 'product'] запишите в файл 'data.csv'.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована."""
import pandas as pd
df = pd.read_csv(
    filepath_or_buffer="data_10.csv",
    sep=",",
    usecols=['client', 'product'],
)

print(df.head())

df.to_csv("data_10_download.csv",
          columns=['client', 'product'],)