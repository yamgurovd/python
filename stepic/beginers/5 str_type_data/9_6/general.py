"""Тема урока: форматирование строк
Строковый метод format()
f-строки
Аннотация. Строковый тип данных, основные методы форматирования строк."""

"""Метод format()
Хранить строки в переменных удобно, но часто бывает необходимо собирать строки из других объектов (строк, чисел и т.д.) 
и выполнять с ними нужные манипуляции. Для этой цели можно воспользоваться механизмом форматирования строк.

Рассмотрим следующий код:"""
birth_year = 1992
text = 'My name is Timur, I was born in ' + birth_year

print(text)

"""Такой код приводит к ошибке во время выполнения программы, поскольку мы пытаемся сложить число и строку:
TypeError: can only concatenate str (not "int") to str"""

"""Для решения такой проблемы мы можем использовать функцию str(), которая преобразует числовое значение в строку.

Приведенный ниже код:"""
birth_year = 1992
text = 'My name is Timur, I was born in ' + str(birth_year)

print(text)

"""выводит:
My name is Timur, I was born in 1992"""

"""Такой код работает, но каждый раз преобразовывать число в строку не очень удобно. 
Для более наглядного форматирования мы можем использовать строковый метод format().

Предыдущий код можно переписать в виде:"""
birth_year = 1992
text = 'My name is Timur, I was born in {}'.format(birth_year)

print(text)

"""Мы передаем необходимые параметры методу format(), а Python ставит их вместо фигурных скобок {} – заполнителей. 
Мы можем создавать сколько угодно заполнителей.

Приведенный ниже код:"""
birth_year = 1992
name = 'Timur'
profession = 'math teacher'
text = 'My name is {}, I was born in {}, I work as a {}.'.format(name, birth_year, profession)

print(text)

"""Для наглядности и гибкости форматирования мы можем использовать порядковый номер в заполнителе: {0}, {1}, {2} и т.д. 
Такой номер определяет позицию параметра, переданного методу format() (нумерация начинается с нуля):"""
birth_year = 1992
name = 'Timur'
profession = 'math teacher'
text = 'My name is {0}, I was born in {1}, I work as a {2}.'.format(name, birth_year, profession)

print(text)

"""Параметр name встает в заполнителе {0}, параметр birth_year – в заполнителе {1} и т.д. 
Мы можем использовать одно и то же число в нескольких заполнителях или не использовать совсем, 
а также мы можем использовать числа в разном порядке.

Приведенный ниже код:"""
name = 'Timur'
city = 'Moscow'
text1 = 'My name is {0}-{0}-{0}!'.format(name, city)
text2 = '{1} is my city and {0} is my name!'.format(name, city)

print(text1)
print(text2)

"""выводит:
My name is Timur-Timur-Timur!
Moscow is my city and Timur is my name!"""

"""f-строки
Метод format() хорошо справляется с задачей форматирования строк, однако если параметров много, 
то код может показаться немного избыточным.

Приведенный ниже код:"""
first_name = 'Taylor'
second_name = 'Swift'
country = 'USA'
birth_date = '1989/12/13'
birth_place = 'West Reading, Pennsylvania'
text = '{0} {1} is a very famous singer from the {2}. She was born on {3} in {4}.'.format(first_name, second_name,
                                                                                          country, birth_date,
                                                                                          birth_place)

print(text)

"""В Python 3.6 появилась новая разновидность строк — f-строки. Если поставить перед строкой префикс f, 
в заполнители можно будет включить код, например, имя переменной или любые другие выражения. f-строки 
обеспечивают чистый и интуитивно понятный способ форматирования строк.

Предыдущий код можно записать в виде:"""
first_name = 'Taylor'
last_name = 'Swift'
country = 'USA'
birth_date = '1989/12/13'
birth_place = 'West Reading, Pennsylvania'
text = f'{first_name} {last_name} is a very famous singer from the {country}. She was born on {birth_date} in {birth_place}.'

print(text)

