"""
Сортировка трёх 🌶️
Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

Примечание. Учитывайте, что числа могут быть равны.
"""

dig_1, dig_2, dig_3 = int(input()), int(input()), int(input())

dig_mx = max(dig_1, dig_2, dig_3)
dig_mn = min(dig_1, dig_2, dig_3)
dig_mdl = (dig_1 + dig_2 + dig_3) - (dig_mx + dig_mn)

print(dig_mx, dig_mdl, dig_mn, sep="\n")