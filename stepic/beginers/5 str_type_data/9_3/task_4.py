"""Нижний регистр
На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.

Формат входных данных
На вход программе подается строка.

Формат выходных данных
Программа должна вывести количество буквенных символов в нижнем регистре.

Алгоритм
1 ввели переменную S
2 счетчик ноль
3. цикл i in range (len(s)):
4. ЕСЛИ "a" <= s[i] <= "z":
5 счетчик +=1
6 выводим счетчик"""


text = input()
counter = 0

for i in range(len(text)):
    if "a" <= text[i] <= "z":
        counter += 1

print(counter)


# Второй способ решения предложенное Гигачатом
# Вводим строку
s = input()

# Подсчитываем количество строчных букв
count = sum(1 for char in s if char.islower())

# Выводим результат
print(count)