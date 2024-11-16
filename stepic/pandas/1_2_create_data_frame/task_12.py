"""Упражнение 12.
В программе созданы две серии и записаны в переменные ser_1 и ser_2.
Сформируйте DataFrame с двумя столбцами, имена столбцов col_1 и col_2.
Столбец col_1 сформируйте на основе данных из ser_1, а col_2 из ser_2.

Результат запишите в переменную df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована."""
import pandas as pd
dct = {
    "col_1": ["ser_1"],
    "col_2": ["ser_2"]
}
df = pd.DataFrame(data=dct)
print(df)


# Второе решение задачи
ser_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ser_2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
len_ser_1 = len(ser_1)
len_ser_2 = len(ser_2)

# Формируем DataFrame
dct = {
    "col_1": ser_1[:len_ser_1],
    "col_2": ser_2[:len_ser_2]
}

df = pd.DataFrame(data=dct)
print(df)