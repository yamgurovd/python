"""Упражнение 3.
Создайте серию с 5 элементами. Индексы строк должны иметь значение row_1, row_2, row_3, row_4, row_5

Результат запишите в переменную series."""
import pandas as pd

lst = {"row_1": 1,
       "row_2": 2,
       "row_3": 3,
       "row_4": 4,
       "row_5": 5}
series = pd.Series(data=lst)
print(series)
