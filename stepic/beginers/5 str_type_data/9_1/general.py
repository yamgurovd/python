"""Тема урока: строки
Индексация строк
Итерирование строк
Решение задач
Аннотация. Строковый тип данных. Вспомним основные операции над строками, научимся работать с отдельными символами,
а также перебирать (итерировать) символы строк.

Повторение материала
Строки в Python используются, когда надо работать с текстовыми данными.

Создание строки. Для создания строк мы используем парные кавычки '' или "":"""
s1 = 'Python'
s2 = "Pascal"

"""Считывание строки. Для считывания текстовых данных в строковую переменную мы используем функцию input():"""
s = input()  # считали текст
num = int(input())  # считали текст и преобразовали его в целое число

"""Пустая строка. Для создания пустой строки мы пишем s = '' или s = "". Пустая строка – это аналог числа 0.
Длина строки. Для определения длины строки (количества символов) мы используем встроенную функцию len():"""
s = 'Hello'
n = len(s)  # значение переменной равно 5
print(n)

"""Конкатенация и умножение на число. Операторы + и * можно использовать для строк. Оператор + сцепляет две и более строк. 
Это называется конкатенацией строк. Оператор * повторяет строку указанное количество раз."""

"""Оператор принадлежности in. С помощью оператора in мы можем проверять, находится ли одна строка в составе другой. 
То есть, является ли одна строка подстрокой другой:"""
s = 'All you need is love'
if 'love' in s:
    print('❤️')
else:
    print('💔')

"""Так как строка s содержит подстроку 'love', то будет выведен смайлик ❤️."""

"""Индексация строк
Очень часто бывает необходимо обратиться к конкретному символу в строке. 
Для этого в Python используются квадратные скобки [], в которых указывается индекс (номер) нужного символа в строке.

Пусть s = 'Python'. Таблица ниже показывает, как работает индексация:"""

"""Выражение	Результат	Пояснение
s[0]	P	первый символ строки
s[1]	y	второй символ строки
s[2]	t	третий символ строки
s[3]	h	четвертый символ строки
s[4]	o	пятый символ строки
s[5]	n	шестой символ строки"""

"""В отличие от многих языков программирования, в Python есть возможность работы с отрицательными индексами. 
Если первый символ строки имеет индекс 0, то последнему элементу присваивается индекс -1.

Выражение	Результат	Пояснение
s[-6]	P	первый символ строки
s[-5]	y	второй символ строки
s[-4]	t	третий символ строки
s[-3]	h	четвертый символ строки
s[-2]	o	пятый символ строки
s[-1]	n	шестой символ строки"""

"""Итерирование строк
Очень часто нужно просканировать всю строку целиком, обрабатывая каждый ее символ. Для этого удобно использовать цикл for. 
Напишем программу, которая выводит каждый символ строки на отдельной строке:"""
s = 'abcdef'
for i in range(len(s)):
    print(s[i])

"""Мы передаем в функцию range() длину строки len(s). В нашем случае длина строки s, равна 
6
6. Таким образом, вызов функции range(len(s)) имеет вид range(6) и переменная цикла i последовательно 
перебирает все значения от 0 до 5. Это означает, что выражение s[i] последовательно вернет все символы строки s. 
Такой способ итерации строки удобен, когда нам нужен не только сам элемент s[i], но и его индекс i.

Если нам не нужен индекс самого символа, то мы можем использовать более короткий способ итерации:"""
s = 'abcdef'
for c in s:
    print(c)