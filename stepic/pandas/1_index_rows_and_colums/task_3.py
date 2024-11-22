"""Упражнение 3

В программе создан DataFrame и записан в переменную df. С помощью специальных свойств DataFrame получите индексы
строк и столбцов и запишите их в соответствующие переменные ind и cols.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована."""
import pandas as pd

df = pd.read_csv(
    filepath_or_buffer="data.csv",
    sep=","
)

# print(df.head())

ind = df.index
cols = df.columns
print(ind, cols, sep="\n")