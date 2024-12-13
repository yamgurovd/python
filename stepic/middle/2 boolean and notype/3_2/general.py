"""Тема урока: тип данных NoneType
Тип данных NoneType
Литерал None
Сравнение None с другими типами данных
Аннотация. Урок посвящен типу данных NoneType."""

"""Пустое значение
Во многих языках программирования (Java, C++, C#, JavaScript и т.д.) существует ключевое слово null, 
которое можно присвоить переменным. Концепция ключевого слова null заключается в том, 
что оно дает переменной нейтральное или "нулевое" поведение.

В языке Python, слово null заменено на None, поскольку слово null звучит не очень дружелюбно, 
а None относится именно к требуемой функциональности – это ничего и не имеет поведения."""

"""Литерал None
Литерал None в Python позволяет представить null переменную, то есть переменную, которая не содержит какого-либо значения. 
Другими словами, None – это специальная константа, означающая пустоту. Если более точно, 
то None – это объект специального типа данных NoneType."""

"""Следующий программный код:"""
var = None
print(type(var))

"""выведет: <class 'NoneType'>"""

"""Мы можем присвоить значение None любой переменной, однако мы не можем самостоятельно создать другой NoneType объект.

Все переменные, которым присвоено значение None, ссылаются на один и тот же объект типа NoneType. 
Создание собственных экземпляров типа NoneType недопустимо. Объекты, существующие в единственном экземпляре, 
называются синглтонами."""

"""Проверка на None
Для того чтобы проверить значение переменной на None, мы используем либо оператор is, 
либо оператор проверки на равенство ==.

Следующий программный код:"""
var = None
if var is None:  # используем оператор is
    print('None')
else:
    print('Not None')

"""выведет: None"""

"""Следующий программный код:"""
var = None
if var == None:  # используем оператор ==
    print('None')
else:
    print('Not None')

"""выведет: None"""

"""Для сравнения переменной с None всегда используйте оператор is. 
Для встроенных типов поведение is и == абсолютно одинаково, однако с пользовательскими типами могут возникнуть проблемы, 
так как в Python есть возможность переопределения операторов сравнения в пользовательских типах."""

"""Сравнение None с другими типами данных
Сравнение None с любым объектом, отличным от None, дает значение False.

Следующий программный код:"""
print(None == None)

"""выведет:True"""

"""Следующий программный код:"""
print(None == 17)
print(None == 3.14)
print(None == True)
print(None == [1, 2, 3])
print(None == 'Beegeek')

"""выведет:

False
False
False
False
False"""

"""Важно понимать, что следующий программный код:"""
print(None == 0)
print(None == False)
print(None == '')

"""выведет:

False
False
False"""

""" Значение None не отождествляется со значениями 0, False, ''.
Сравнивать None с другими типами данных можно только на равенство.
Следующий программный код:"""
print(None > 0)
print(None <= False)

"""приводит к ошибке: TypeError: '>' not supported between instances of 'NoneType' and 'int' ('bool')"""


"""Примечания
Примечание 1. Обратите внимание, что функции, не возвращающие значений, на самом деле, в Python возвращают значение None:"""


def print_message():
    print('Я - Тимур,')
    print('король матана.')


"""Мы можем вызвать функцию print_message() так: 

print_message()
 или так:

res = print_message()
В переменной res хранится значение None.

Примечание 2. Концепция null значений появилась при создании языка ALGOL W великим Чарльзом Хоаром,
который позднее назвал собственную идею ошибкой на миллиард долларов. Подробнее можно почитать тут."""
