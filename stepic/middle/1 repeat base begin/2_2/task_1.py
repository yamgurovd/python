"""Координатные четверти
Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек,
лежащих в каждой координатной четверти.

Формат входных данных
В первой строке записано количество точек. Каждая следующая строка состоит
из двух целых чисел — координат точки (сначала абсцисса – x, затем ордината – y), разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой-либо координатной четверти."""

n = int(input())  # Число точек
count1 = 0  # Первая четверть
count2 = 0  # Вторая четверть
count3 = 0  # Третья четверть
count4 = 0  # Четвертая четверть

for _ in range(n):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        count1 += 1  # Первая четверть
    elif x < 0 and y > 0:
        count2 += 1  # Вторая четверть
    elif x < 0 and y < 0:
        count3 += 1  # Третья четверть
    elif x > 0 and y < 0:
        count4 += 1  # Четвертая четверть

print("Первая четверть:", count1)
print("Вторая четверть:", count2)
print("Третья четверть:", count3)
print("Четвертая четверть:", count4)

# Второй способ решения задачи
# put your python code here
n = int(input())
coordinates = []
quarter = [0] * 4
titles = ['Первая четверть', 'Вторая четверть',
          'Третья четверть', 'Четвертая четверть']
for i in range(n):
    coordinates.append(input().split())

for coordinate in coordinates:
    x = int(coordinate[0])
    y = int(coordinate[1])
    if x > 0 and y > 0:
        quarter[0] += 1
    elif x < 0 and y > 0:
        quarter[1] += 1
    elif x < 0 and y < 0:
        quarter[2] += 1
    elif x > 0 and y < 0:
        quarter[3] += 1

for i in range(len(quarter)):
    print(f'{titles[i]}: {quarter[i]}')

# Третий способ решения задачи
cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
for c in range(int(input())):
    x, y = list(map(int, input().split()))
    cnt1 += int(x > 0 and y > 0)
    cnt2 += int(x < 0 and y > 0)
    cnt3 += int(x < 0 and y < 0)
    cnt4 += int(x > 0 and y < 0)

print(f"Первая четверть: {cnt1}\nВторая четверть: {cnt2}\nТретья четверть: {cnt3}\nЧетвертая четверть: {cnt4}")
