"""Стоимость ответа 💬
Модератору Сэму за каждый символ его сообщений в комментариях Тимур платит в 🐝 (пчелках-coin) по следующему тарифу:

<код символа в таблице Unicode>×3🐝<код символа в таблице Unicode>×3🐝

А стоимость всего сообщения складывается из суммы стоимостей всех символов. Сэму захотелось подсчитать, сколько 🐝
он зарабатывает за свои ответы в комментариях, и просит вас помочь ему.

На вход программе подается строка текста. Требуется написать программу, которая находит стоимость сообщения Сэма в 🐝 и
выводит текст в следующем формате:

Текст сообщения: '<текст сообщения Сэма>'
Стоимость сообщения: <стоимость сообщения Сэма>🐝
Формат входных данных
На вход программе подается строка текста – очередной ответ Сэма в комментариях.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. 🐝 (пчелка-coin) – виртуальная валюта команды BEEGEEK, которой Тимур расплачивается со своими сотрудниками."""

text = input()

cost = [ord(i) * 3 for i in text]

cost_ = 0
for i in cost:
    cost_ += i

print(f"""Текст сообщения: '{text}'
Стоимость сообщения: {cost_}🐝""")

# Второй и третий способ решения - взято из форума
message = input()
cost = 0

for c in message:
    cost += ord(c) * 3

print(f"Текст сообщения: '{message}'")
print(f'Стоимость сообщения: {cost}🐝')


print(f"Текст сообщения: '{(text := input())}'")
print(f"Стоимость сообщения: {3 * sum(ord(i) for i in text)}🐝")
