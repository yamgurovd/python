"""Упражнение 6.

В программе создан DataFrame и записан в переменную df. С помощью специального свойства определите есть ли
пропуски в индексах строк.

В переменную nan_in_indx запишите True если пропуски есть и False если пропусков нет.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована."""
import pandas as pd

df = pd.read_csv(
    filepath_or_buffer="data_6.csv",
    sep=",",
    header=0,
)
rows = [f"row_{i+1}"for  i in range(len(df))]


df.index = rows
# print(df)

if df.index.hasnans:
    nan_in_indx = True
else:
    nan_in_indx = False

# print(nan_in_indx)


"""Обработка данных таблицы"""
# Первый способ
# for i in range(df.shape[0]):
#     print(df.iloc[i])

# Второй способ
# for i in df.to_dict():
#     print(df[i], end=" ")


conv = df.to_dict()


for i in conv.values():
    print(i)

# print(df.get("city", "There is no key"))