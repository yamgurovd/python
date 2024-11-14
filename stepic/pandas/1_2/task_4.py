"""Упражнение 4.
Создайте серию с 5 элементами и именем(имя придумайте сами).
Индексы строк должны иметь значение row_1, row_2, row_3, row_4, row_5.

Результат запишите в переменную series."""
import pandas as pd
dct = {
"row_1": "test 123",
    "row_2": "test 124",
    "row_3": "test 125",
    "row_4": "test 126",
    "row_5": "test 127",
}
series = pd.Series(dct, dtype="string", name="series")
print(series)