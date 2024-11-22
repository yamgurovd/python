"""Упражнение 4.

В программе создан DataFrame и записан в переменную df. Получите список с индексами строк и список с индексами
столбцов и запишите их в переменные list_ind и list_cols.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована."""
import pandas as pd
df = pd.read_csv(
    filepath_or_buffer="data_4.csv",
    sep=","
)

print(df.head())

list_ind = df.index.to_list()
list_cols = df.columns.to_list()
print(list_ind, list_cols, sep="\n")