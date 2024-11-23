"""Дополните приведенный код, используя срезы, так чтобы он вывел каждый 7 символ строки s (начиная с 0-го индекса)."""
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[::7])

# Второй способ решения
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
for i in range(len(s)):
    if i % 7 == 0:
        print(s[i], end='')