"""
Тернарный условный оператор

Рассмотрим такой пример для сравнения двух чисел и получения большего из них:
"""
a = 42
b = 41

if a > b:
    result = a
else:
    result = b

"""
Данный код в зависимости от значения переменых а и b присваивает переменной result значение большей из них. 
Код сравнения занимает аж 4 строки, а выполняет элементарное действие. Это не в стиле Python, нужно исправлять 
данную ситуацию. Для таких случаев существует так называемый тернарный условный оператор — оператор, 
который записывается в одну строку. В Python вы можете встретить название «инлайновый if». 
Тогда код можно будет переписать следующим образом:
"""

result = a if a > b else b

"""
Хорошо написанный код можно буквальным образом читать, в данном случае эту строку можно прочитать как: 
«Присвой переменной result значение a, если a больше b, в противном случае присвой значение b». Просто, не правда ли?
"""

