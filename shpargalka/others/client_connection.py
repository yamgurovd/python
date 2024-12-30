import socket
import pickle

"""Клиент (постоянное слушание задач)
Теперь клиент будет ждать задания от сервера в цикле и завершится только тогда, когда получит None в качестве задания."""

# Параметры сервера
SERVER_HOST = '192.168.0.1'  # IP-адрес сервера
SERVER_PORT = 12345


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("[INFO] Connected to the server.")

        while True:
            # Получаем данные задачи от сервера
            data = client_socket.recv(1024)
            task_data = pickle.loads(data)

            # Проверяем, нет ли команды на завершение
            if task_data is None:
                print("[INFO] No more tasks. Shutting down.")
                break

            # Выполняем задание
            result = task_data ** 2  # Пример: возведение числа в квадрат

            # Отправляем результат серверу
            client_socket.send(pickle.dumps(result))


if __name__ == "__main__":
    client()
