# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб

result: dict = dict(zip([i for i in range(10)], [i**3 for i in range(10)]))

print(f"Результат: {result}")