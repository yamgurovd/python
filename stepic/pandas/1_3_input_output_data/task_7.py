"""Упражнение 9.

В программе создан файл с данными - "data.csv".

:city:col_2:col_3:date:col_5
0:Москва:20:347:2018-04-27:True
1:Санкт-Петербург:40:637:2018-10-10:False
2:Ярославль:20:326:2018-08-13:True
3:Вологда:40:691:2017-05-13:False
4:Омск:20:327:2016-10-17:False
5:Ногород:40:601:2016-09-17:True
Импортируйте данные из файла и присвойте столбцу 'city' тип данных 'category', столбцу 'col_2' - 'string', а 'col_3' -
'int'. Столбец 'date' установите в качестве индексов строк.

Результат запишите в переменную df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована."""
import pandas as pd
df = pd.read_csv(
    filepath_or_buffer="data_7.csv",
    sep=":",
    index_col="date",
    usecols=["city", "col_2", "col_3", "date"],
    dtype={
        "city": "category",
        "col_2": "string",
        "col_3": "int",
    }
)

print(df)


# Второй способ решения задачи от Гигачат
# Чтение данных из CSV-файла
df = pd.read_csv("data_7.csv", sep=":")

# Установка типов данных для столбцов
df["city"] = df["city"].astype("category")
df["col_2"] = df["col_2"].astype("string")
df["col_3"] = df["col_3"].astype("int")

# Установка столбца 'date' в качестве индекса
df.set_index(pd.to_datetime(df["date"], format="%Y-%m-%d"), inplace=True)

# Удаление исходного столбца 'date', так как он стал индексом
del df["date"]

# Результат записан в переменную df