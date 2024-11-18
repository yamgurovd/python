"""Упражнение 11.

В программе создан DataFrame и записан в переменную df. Запишите df в файл 'data.csv'.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована."""
import pandas as pd
df = pd.read_csv(
    filepath_or_buffer="data_9.csv",
    sep=","
)

print(df)

df.to_csv("data_9_download.csv", index=False)