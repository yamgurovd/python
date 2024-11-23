# Первый  пример - функция как аргумент другой функции
def func_1(
        func: str) -> str:
    func = func
    return func


def func_2(
        a: int,
        b: int) -> int:
    return a + b


a = func_1(func=func_2(1, 1))
print(a)

# Второй пример
def func_3(func):

    def wrapper(*args, **kwargs, ):
        print("First")
        result = func(*args, **kwargs)
        print("Second")

        return result
    print("Third")
    return wrapper


b = func_3(func=func_2(1, 1))

# Третий пример с использованием мэджик
@func_3
def func_4(a: int, b: int) -> int:
    return a * b

c = func_4(1, 2)


# Замыкание пример взят из гигачата
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


hi_func = outer_function('Привет!')
bye_func = outer_function('До свидания!')

hi_func()  # Выведет 'Привет!'
bye_func()  # Выведет 'До свидания!'


# Пример декоратора, взято из гигачата
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Перед вызовом функции")
        result = func(*args, **kwargs)
        print("После вызова функции")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Привет, {name}!")

greet("Иван")