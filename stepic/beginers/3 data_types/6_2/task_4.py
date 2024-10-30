"""
Три города 🏙️
Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаются названия трёх городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трёх городов различны.
"""

city_1, city_2, city_3 = input(), input(), input()

len_city_1, len_city_2, len_city_3 = len(city_1), len(city_2), len(city_3)

if min(len_city_1, len_city_2, len_city_3) == len_city_1:
    print(city_1)
elif min(len_city_1, len_city_2, len_city_3) == len_city_2:
    print(city_2)
elif min(len_city_1, len_city_2, len_city_3) == len_city_3:
    print(city_3)

if max(len_city_1, len_city_2, len_city_3) == len_city_1:
    print(city_1)
elif max(len_city_1, len_city_2, len_city_3) == len_city_2:
    print(city_2)
elif max(len_city_1, len_city_2, len_city_3) == len_city_3:
    print(city_3)

# Второй вариант решения
# put your python code here
# frt = input()
# scd = input()
# trd = input()
# dic = {len(frt): frt, len(scd): scd, len(trd): trd}
#
# min_ct = min(len(frt), len(scd), len(trd))
# max_ct = max(len(frt), len(scd), len(trd))
#
# print(dic[min_ct])
# print(dic[max_ct])
