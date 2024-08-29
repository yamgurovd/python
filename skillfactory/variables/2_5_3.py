"""
Как должен выглядеть шаблон строки для вывода времени в записанном ниже формате?

HH:MM:SS
Вставьте нужный шаблон вместо знаков "???", используя только специальный символ «%d».
print("???" % (hours, minutes, seconds))
Вам необходимо вывести время в таком формате, чтобы перед однозначным числом в выводе стоял ноль.
Пример: 01:02:03.

Примечание
Для каждого типа данных существует свой специальный символ:

Формат	Тип данных
%d, %i	Целое число
%5d, %12d	Выделяет пространство 5 (или любое другое число) символов под это число. Выравнивание вправо, остальное пространство остаётся пустым
%05d	Также выделяется пространство в 5 символов, но свободное пространство слева заполняется нулями
%o	Число в восьмеричной системе счисления
%x	Число в шестнадцатеричной системе счисления
%f	Число с плавающей точкой
%10.2f	Число с плавающей точкой, для которого зарезервировано пространство из 10 символов и стоит ограничение на количество знаков после запятой — 2
%e	Также число с плавающей точкой, но в экспоненциальной записи
%c	Код символа
%s	Другая строка
%%	Знак процента, если его необходимо использовать



day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2
"""
hours = 00
minutes = 00
seconds = 00

print("%02d:%02d:%04d" % (hours, minutes, seconds))