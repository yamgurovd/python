n = int(input())
flag = 'YES'
lst = []

for i in range(n):
    s2 = input()
    s3 = s2.replace(s2[s2.find(' '):s2.find('«')], '')
    lst.append(s3)
for i in range(1, len(lst)):
    if lst[i] <= lst[i - 1]:
        flag = 'NO'

print(flag)

# Второй способ решения задачи - взято из форума
n = int(input())

# переменные для хранения предыдущей фамилии автора и названия книги
previous_book = ''
# переменная флага указывает, сохранен ли порядок сортировки книг:
is_ordered = 'YES'

for i in range(n):
    s = input()
    # извлекаем фамилию автора до первого пробела
    current_surname = s[: s.find(' ')]
    # извлекаем название книги между кавычками «»
    current_title = s[s.find('«') + 1: s.rfind('»')]
    # склеиваем фамилию автора и название книги
    current_book = current_surname + current_title

    # если текущая книга меньше предыдущей
    # то порядок сортировки нарушен
    if current_book < previous_book:
        is_ordered = 'NO'

    # обновляем предыдущие значения книги на текущие
    previous_book = current_book

print(is_ordered)


# Третий способ решения  взято - Гигачат
def is_sorted_books(n, books):
    sorted_books = sorted(books, key=lambda x: (x.split()[0], x.split(', «')[1][:-1]))

    if books == sorted_books:
        return "YES"
    else:
        return "NO"


# Чтение количества книг
n = int(input())

# Чтение списка книг
books = []
for _ in range(n):
    books.append(input().strip())

# Проверка и вывод результата
print(is_sorted_books(n, books))
