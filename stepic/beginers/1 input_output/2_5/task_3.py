"""
 Мандарины 🍊
n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине.
Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?

Формат входных данных
На вход программе подаётся два целых числа: количество школьников и количество мандаринов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два числа: количество мандаринов,
которое достанется каждому школьнику, и количество мандаринов, которое останется в корзине, каждое на отдельной строке.
"""

students = int(input())
mandarins = int(input())

count_mandarins_students = mandarins // students
print(count_mandarins_students)

count_mandarins_cart = mandarins % students
print(count_mandarins_cart)
