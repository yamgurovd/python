"""12 месяцев
Решите уравнение в натуральных числах 28n+30k+31m=365.

Примечание. Используйте вложенный цикл for. В первую очередь запишите решение с наименьшим значением n."""

def find_solution():
    for n in range(1, 13):  # Максимальное возможное значение n
        for k in range(1, 13):  # Максимальное возможное значение k
            if 28*n + 30*k > 365:
                break
            m = (365 - 28*n - 30*k) / 31
            if m.is_integer() and m > 0:
                return n, k, int(m)

solution = find_solution()
if solution is not None:
    n, k, m = solution
    print(f"Решение найдено: n={n}, k={k}, m={m}")
else:
    print("Нет решений.")