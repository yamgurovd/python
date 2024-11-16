"""Упражнение 8.
Создайте DataFrame содержащий 3 столбца и 3 строки, индексы строк должны иметь следующие имена: row_1, row_2, row_3.

Результат запишите в переменную df."""
import pandas as pd

dict_in = {
    "row_1": [1, "test 123", 11.99],
    "row_2": [2, "test 124", 22.00],
    "row_3": [3, "test 125", 33.11]
}
index_ = ['row_1', 'row_2', 'row_3']
df = pd.DataFrame(data=dict_in, index=index_)
print(df)
