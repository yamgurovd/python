x = 100


def change_var():
    print(x)
    global x
    x = 5
    print(x)


change_var(x)
print(x)
