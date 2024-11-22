"""Упражнение 2

Создайте объект класса Index с 4-мя элементами и именем "my_index".

Результат запишите в переменную ind."""
import pandas as pd

my_index = ["a", "b", "c", "d"]

ind = pd.Index(data=my_index, name="my_index")
print(ind)
