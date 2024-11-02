# Сгенерировать список от 0 до 100 отсортированный на убывание, где числа нечетные и кратны 3
result: list = [i for i in range(0, 100, 3)]

print(f"Результат: {sorted(result, reverse=True)}\n")
