"""Дополните приведенный код, используя списочный метод append(), чтобы список list1 имел вид:

list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]"""
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1 = []
list1.append(10)
list1.append(20)

list2 = []
list2.append(300)
list2.append(400)

list3 = []
list3.append(5000)
list3.append(6000)
list3.append(7000)

list2.append(list3)
list2.append(500)

list1.append(list2)
list1.append(30)
list1.append(40)

print(list1)

# ВТорой способ решения задачи
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
