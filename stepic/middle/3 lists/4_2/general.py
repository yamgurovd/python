"""Тема урока: вложенные списки
Вложенные списки
Объявление и индексация
Функции len(), max(), min()
Списочные методы
Аннотация. Урок посвящен вложенным спискам, то есть спискам, входящим в качестве элементов в другие списки."""

"""Введение
Как мы уже знаем, список представляет собой упорядоченную последовательность элементов, индексы которых пронумерованы от 0. 
Элементами списка могут быть любые типы данных – числа, строки, булевы значения и т.д. Например,"""
numbers = [10, 3]
constants = [3.1415, 2.71828, 1.1415]
countries = ['Russia', 'Armenia', 'Argentina']
flags = [True, False]

"""Список numbers состоит из 2-х элементов, и каждый из них — целое число:

numbers[0] == 10;
numbers[1] == 3.
Список constants состоит из 3-х элементов, каждый из которых — вещественное число:

constants[0] == 3.1415;
constants[1] == 2.71828;
constants[2] == 1.1415.
Список countries состоит из 3-х элементов, каждый из которых — строка:

countries[0] == 'Russia';
countries[1] == 'Armenia';
countries[2] == 'Argentina'.
Список flags состоит из 2-х элементов, и каждый из них — булево значение:

flags[0] == True;
flags[1] == False."""

"""Мы также говорили, что элементы списка не обязательно должны иметь одинаковый тип данных. 
Список может содержать значения разных типов данных:"""
info = ['Timur', 1992, 72.5]

"""Список info содержит строковое значение, целое число и число с плавающей точкой:

info[0] == 'Timur';
info[1] == 1992;
info[2] == 72.5."""

"""Обычно элементы списка содержат данные одного типа, и на практике редко приходится создавать списки, 
содержащие элементы разных типов данных."""

"""Вложенные списки
Оказывается, элементами списков могут быть другие списки и в реальной разработке такая конструкция 
оказывается очень полезной. Такие списки называются вложенными списками.

Создание вложенного списка
Работа с вложенными списками принципиально ничем не отличается от работы со списками, например, чисел или строк. 
Чтобы создать вложенный список, мы также перечисляем элементы через запятую в квадратных скобках:"""
my_list = [[0], [1, 2], [3, 4, 5]]

"""Переменная my_list ссылается на список, состоящий из других списков (с вложенными списками).

Поскольку глубина вложенности списка my_list равна двум, то такой список обычно называют двумерным списком. 
На практике, как правило, мы работаем с двумерными списками, реже – с трехмерными.

Рассмотрим программный код:"""
my_list = [[0], [1, 2], [3, 4, 5]]

print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(len(my_list))

"""Результатом работы такого кода будет:

[[0], [1, 2], [3, 4, 5]]
[0]
[1, 2]
[3, 4, 5]
3"""

"""Давайте взглянем на каждую строку приведенного кода поближе.

строка 1 создает список и присваивает его переменной my_list. Список имеет три элемента, и каждый элемент тоже является списком:
элементом my_list[0] является список [0];
элементом my_list[1] является список [1, 2];
элементом my_list[2] является список [3, 4, 5].
строка 3 распечатывает весь список my_list;
строка 4 распечатывает элемент my_list[0];
строка 5 распечатывает элемент my_list[1];
строка 6 распечатывает элемент my_list[2];
строка 7 распечатает количество элементов списка my_list, то есть число 3."""

"""Индексация
При работе с одномерными списками мы использовали индексацию, то есть обращение к конкретному элементу по его индексу. 
Аналогично можно индексировать и вложенные списки:"""
my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik']]

print(my_list[0])
print(my_list[1])
print(my_list[2])

"""Результатом работы такого кода будет:

Python
[10, 20, 30]
['Beegeek', 'Stepik']"""

"""Так как элементы списка my_list – строка и списки, их также можно индексировать.

Рассмотрим программный код:"""
my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik!']]

print(my_list[0][2])  # индексирование строки 'Python'
print(my_list[1][1])  # индексирование списка [10, 20, 30]
print(my_list[2][-1])  # индексирование списка ['Beegeek', 'Stepik!']
print(my_list[2][-1][-1])  # индексирование строки 'Stepik!'

"""Результатом работы такого кода будет:
t
20
Stepik!
!"""

"""Попытка обратиться к элементу списка по несуществующему индексу:"""
print(my_list[3])  # у списка my_list индексы от 0 до 2

"""вызовет ошибку: IndexError: index out of range"""

"""Функции len(), max(), min()
В прошлом курсе мы рассматривали встроенные функции max(), min(), len(), 
полезные и при работе с вложенными списками (обработке вложенных списков).

 Функция len()
Рассмотрим программный код:"""
my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]

print(len(my_list))

"""Результатом работы такого кода будет: 5"""

"""Обратите внимание, встроенная функция len() возвращает количество элементов (число 5) списка my_list, 
а не общее количество элементов во всех списках (число 9).

Если требуется посчитать общее количество элементов во вложенном списке my_list, 
мы можем использовать цикл for в связке с функцией len():"""
total = 0
my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]

for li in my_list:
    total += len(li)

print(total)

"""Результатом работы такого кода будет: 9"""

"""Переменная li последовательно принимает все значения элементов списка my_list, то есть является сама по себе списком, 
поэтому мы можем вызывать функцию len() с переданным аргументом li.

Функции min() и max()
Функции min() и max() могут работать и со списками. Если этим функциям передается несколько списков, 
то целиком возвращается один из переданных списков. При этом сравнение происходит поэлементно: 
сначала сравниваются первые элементы списков. Если они не равны, то функция min() вернет тот список, 
первый элемент которого меньше, max() – наоборот. Если первые элементы равны, то будут сравниваться вторые и т. д.

Рассмотрим программный код:"""
list1 = [1, 7, 12, 0, 9, 100]
list2 = [1, 7, 90]
list3 = [1, 10]

print(min(list1, list2, list3))
print(max(list1, list2, list3))

"""Результатом работы такого кода будет:

[1, 7, 12, 0, 9, 100]
[1, 10]"""

"""Функции min() и max() также можно использовать при работе с вложенными списками. Рассмотрим программный код:"""
list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]

print(min(list1))
print(max(list1))
print(min(list2))
print(max(list2))

"""Результатом работы такого кода будет:

[1, 7, 12, 0, 9, 100]
[1, 10]
['a']
['d', 'p', 'q']"""

"""Обратите внимание – элементы вложенных списков в этой ситуации должны быть сравнимы.

Таким образом, следующий код:"""
my_list = [[1, 7, 12, 0, 9, 100], ['a', 'b']]

print(min(my_list))
print(max(my_list))

"""приведет к возникновению ошибки: TypeError: '<' not supported between instances of 'str' and 'int'"""

"""Примечания
Примечание 1. Независимо от вложенности списков, нам нужно помнить по возможности все списочные методы:

метод append() добавляет новый элемент в конец списка;
метод extend() расширяет один список другим списком;

метод insert() вставляет значение в список в заданной позиции;

метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению;

метод remove() удаляет первый элемент, значение которого равняется переданному в метод значению;

метод pop() удаляет элемент по указанному индексу и возвращает его;

метод count() возвращает количество элементов в списке, значения которых равны переданному в метод значению;

метод reverse() инвертирует порядок следования значений в списке, то есть меняет его на противоположный;

метод copy() создает поверхностную копию списка.;

метод clear() удаляет все элементы из списка;

оператор del позволяет удалять элементы списка по определенному индексу.

Примечание 2. Методы строк, работающие со списками:

метод split() разбивает строку на слова, используя в качестве разделителя последовательность 
пробельных символов, символ табуляции (\t) или символ новой строки (\n).
метод join() собирает строку из элементов списка, используя в качестве разделителя строку, к которой применяется метод.
Примечание 3. Язык Python не ограничивает нас в уровнях вложенности: элементами списка могут быть списки, 
их элементами могут быть другие списки, элементами которых в свою очередь могут быть другие списки..."""
