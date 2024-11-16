"""Упражнение 5.
На основе указанного словаря dict_in = {'row_1': 1, 'row_2': 2, 'row_3': 3, 'row_4': 4} создайте серию,
содержащую только строки row_2 и row_4.

Результат запишите в переменную series."""
import pandas as pd
dict_in = {'row_1': 1,
           'row_2': 2,
           'row_3': 3,
           'row_4': 4}

series = pd.Series(dict_in, index=['row_2', 'row_4'])
print(series)