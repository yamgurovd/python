"""Дополните приведенный код списочным выражением, чтобы получить новый список,
содержащий только слова длиной не менее пяти символов (включительно)."""
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lst = [i for i in keywords if len(i) >= 5]

print(lst)

# Второй способ решения задачи - взято из форума решений
b = []
for i in range(len(keywords)):
    if len(keywords[i]) >= 5:
        b.append(keywords[i])
print(b)
