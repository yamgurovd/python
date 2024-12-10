# Пример взят от репетитора
from contextlib import AbstractContextManager


class FileManager(AbstractContextManager):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            raise
        except IOError as e:
            print(f"Error: Unable to open file '{self.filename}'. {e}")
            raise
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            try:
                self.file.close()
            except IOError as e:
                print(f"Error: Unable to close file '{self.filename}'. {e}")
                raise e
            else:
                print("adad")
            finally:
                print("ssdfdsfsdf")

        if exc_type:
            print(f"An error occurred: {exc_value}")
            return False

        return True


with FileManager("example.txt", "w") as f:
    f.write("Hello, world!")


class TestContextManager(AbstractContextManager):
    def __init__(self, test_func):
        self.test_func = test_func
        print(self.test_func)

    def __enter__(self):
        self.test_func = 23
        print("enter")

    def __exit__(self, type, value, traceback):
        print("exit")


with TestContextManager(test_func="test_func") as ctx:
    print(ctx)
