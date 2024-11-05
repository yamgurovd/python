# пример 1
n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')


# Пример 2
result = 0
for i in range(10):
    if i % 2 == 0:
        continue
    result += i

print(result)