"""Функция ord()
Функция ord() позволяет определить код некоторого символа в таблице символов Unicode.
Аргументом данной функции является одиночный символ.

Приведенный ниже код:"""
num1 = ord('A')
num2 = ord('B')
num3 = ord('a')
print(num1, num2, num3)

"""выводит: 65 66 97"""

"""Обратите внимание, что функция ord() принимает именно одиночный символ. Если попытаться передать строку, 
содержащую более одного символа, мы получим ошибку времени выполнения.

Приведенный ниже код:
num = ord('Abc')
print(num)

приводит к возникновению ошибки:

TypeError: ord() expected a character, but string of length 3 found"""

"""Название функции ord() происходит от английского слова «order» — порядок."""

"""Функция chr()
Функция chr() позволяет определить по коду символа сам символ. Аргументом данной функции является численный код.

Приведенный ниже код:"""
chr1 = chr(65)
chr2 = chr(75)
chr3 = chr(110)

print(chr1, chr2, chr3)

"""выводит: A K n"""


"""Функции ord() и chr() часто работают в паре. Мы можем использовать следующий код для вывода всех заглавных букв английского алфавита:

for i in range(26):
    print(chr(ord('A') + i))
Приведенный выше код выводит:

A
B
C
...
X
Y
Z
"""

"""Примечания
Примечание 1. Функции ord() и chr() являются взаимно обратными. Для них выполнены равенства:

chr(ord(<символ>)) = <символ>

ord(chr(<код символа>)) = <код символа>

Например, ord('A') возвращает число 65, а chr(65) возвращает символ 'A'. То есть chr(ord('A')) возвращает символ A. 
В обратную сторону это также работает: ord(chr(65)) возвращает число 65.

Приведенный ниже код:"""

print(chr(ord('A')) == 'A')
print(ord(chr(65)) == 65)
"""выводит:

True
True"""

"""Примечание 2. Обратите внимание, что некоторые символы могут выглядеть одинаково, но на самом деле иметь разные 
коды в таблице Unicode. Это в первую очередь касается букв, которые имеют одинаковое написание на разных языках.
"""
"""Приведенный ниже код:
"""
print(ord('a'))     # английская буква «a»
print(ord('а'))     # русская буква «а»
"""выводит:

97
1072
Также можно заметить, что в таблице Unicode русские буквы находятся гораздо дальше английских."""