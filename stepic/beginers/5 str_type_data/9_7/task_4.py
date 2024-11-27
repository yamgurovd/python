"""Самое тяжелое слово 🗿
Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова. Напишите программу,
которая принимает 4 слова и находит среди них самое тяжелое слово. Если самых тяжелых слов будет несколько,
то программа должна вывести первое из них.

Формат входных данных
На вход программе подаются 4 слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое тяжелое слово в строке."""

word_1, word_2, word_3, word_4 = input(), input(), input(), input(),

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0

for i in word_1:
    count_1 += ord(i)


for i in word_2:
    count_2 += ord(i)

for i in word_3:
    count_3 += ord(i)

for i in word_4:
    count_4 += ord(i)

heavy_word = max(count_1, count_2, count_3, count_4)

print()

# Второй способ решения задачи- взято из форума
mx_weight = 0
mx = ''
for word in [input() for _ in range(4)]:
    weight = sum([ord(i) for i in word])
    if mx_weight < weight:
        mx_weight = weight
        mx = word
print(mx)