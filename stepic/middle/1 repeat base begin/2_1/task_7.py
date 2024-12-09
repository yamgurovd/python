"""Standard American Convention
На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые
в соответствии со стандартным американским соглашением о запятых в больших числах.

Формат входных данных
На вход программе подается натуральное число n (0<n<10**100).

Формат выходных данных
Программа должна вывести число с запятыми в соответствии с условием задачи."""
num = input()
num_reverse = num[::-1]
parts = []

for i in range(0, len(num_reverse), 3):
    parts.append(num_reverse[i:i + 3])

formated_ = ','.join(parts)[::-1]

print(formated_)

# Второй способ решения задачи - взято из форума
# put your python code here
num = list(input())
for i in range(len(num) - 3, 0, -3):
    num.insert(i, ',')
print(*num, sep='')
