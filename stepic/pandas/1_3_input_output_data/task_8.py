"""Упражнение 10.

В программе создан файл с данными - "data.csv".

,city,col_2,col_3,date,col_5
0,Москва,20,347,2018-04-27,True
1,Санкт-Петербург,40,637,2018-10-10,False
2,Ярославль,20,326,2018-08-13,True
3,Вологда,40,691,2017-05-13,False
4,Омск,20,327,2016-10-17,False
5,Ногород,40,601,2016-09-17,True

Импортируйте 5 строк из столбцов ['col_2', 'col_3', 'col_5'] и представьте их в виде DataFrame.

Результат запишите в переменную df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована."""
import pandas as pd

df = pd.read_csv(
    filepath_or_buffer="data_8.csv",
    sep=",",
    usecols=["col_2", "col_3", "col_5"],
)

print(df.head())
