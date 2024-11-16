"""Упражнение 2.
Создайте серию состоящую из 4 строк, значения в строках выберите самостоятельно.

Результат запишите в переменную series."""
import pandas as pd


lst = ["str1", "str2", "str3", "str4"]
series = pd.Series(lst, dtype="string")
print(series)