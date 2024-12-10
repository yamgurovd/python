import datetime
from typing import Callable
import time


def decorator_test(func: Callable) -> callable:
    def wrapper(*args, **kwargs):
        print("Start Wrapper!")
        time1 = datetime.datetime.now()
        print(time1)
        func_ = func(*args, **kwargs)
        print("End Wrapper!")

        return func_

    return wrapper


@decorator_test
def get_name(name: str) -> str:
    return f"Hello {name}"


@decorator_test
def check_time() -> any:
    time.sleep(5)
    time2 = datetime.datetime.now()
    print(time2)
    return time2


print(get_name("Ivan"))
print(check_time())


def func1(func):
    def wrapper(*args, **kwargs, ):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    print("End2")

    return wrapper


@func1
def func2(word: str) -> str:
    # print(word)
    return f"Это слово будут написано внутри декоратора {word}"


a = func2(word="Hello World!")
print(a)
