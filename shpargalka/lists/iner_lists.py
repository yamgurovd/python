"""ПРИМЕР РАЗБИВКИ ТЕКСТА НА ВЛОЖЕННЫЕ СПИСКИ - ВЗЯТО ИЗ ЗАДАЧИ - 4_3 - 7 ЗАДАЧА"""

"""Разбиение на чанки 🌶️
Sample Input 1:

a b c d e f
2
Sample Output 1:

[['a', 'b'], ['c', 'd'], ['e', 'f']]"""

def chunked(iterable, n):
    """Разбивает список на чанки заданного размера."""
    chunks = []  # Список для хранения чанков
    for i in range(0, len(iterable), n):
        # Добавляем в список чанк из n элементов
        chunks.append(iterable[i:i + n])
    return chunks

# Ввод данных
input_string = input()
n = int(input())

# Формируем список из введенной строки
elements = input_string.split()

# Вызываем функцию chunked и выводим результат
result = chunked(elements, n)
print(result)