# O (1)
# O (log(n) - бинарный поиск
# O (n)
# O (n*log(n)) - сортировки быстрые, *почитать

# O (n2)
# O(nx)
# O (n!)


# бинарный поиск
# поиск в глубину
# поиск в ширину

list_ = [15, 45, 84, 41, 1, 18, 55, 89, 456, 11, 13, 14, 7, 487, 123, 445]

sorted(list_)


def binary_search(arr: list, x: int):
    begin = 0
    last = len(arr) - 1
    middle = 0
    while begin <= last:
        middle = (begin + last) // 2
        if arr[middle] < x:
            begin = middle + 1
        elif arr[middle] > x:
            begin = middle - 1
        else:
            return middle

    return -1



x = 10

print(binary_search(arr=list_, x=x))

