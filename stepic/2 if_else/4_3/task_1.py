"""
Гонка спидстеров
Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара.
В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, поэтому Флэш решил не рисковать
без причины и узнать у своего друга Циско Рамона, есть ли смысл принимать вызов. Циско получил данные,
что скорость Зума равна n, а скорость Флэша равна k.

Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.

Формат входных данных
На вход программе подаются два целых числа n и k – скорости Зума и Флэша.

Формат выходных данных
Если Зум быстрее Флэша, нужно вывести «NO», а если Флэш быстрее Зума, нужно вывести «YES». В случае же если их скорости равны,
нужно вывести «Don't know».
"""

n, k = int(input()), int(input())

if n > k:
    print('NO')
elif k > n:
    print('YES')
else:
    print("Don't know")
