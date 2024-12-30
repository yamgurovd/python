import socket
import pickle
from multiprocessing import Process


"""Чтобы клиент оставался подключённым к серверу и слушал новые задачи постоянно, можно изменить логику клиента, 
добавив цикл, который будет поддерживать соединение и обрабатывать задачи до тех пор, пока не придёт команда завершения.

Вот как это можно сделать:

Сервер (распределение задач)
Мы добавим возможность отправлять команду None для завершения работы клиента."""

# Параметры сервера
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12345
NUM_TASKS = 10


# Пример задачи
def perform_task(data):
    # Например, возведение числа в квадрат
    return data ** 2


def handle_client(conn, addr):
    print(f"[INFO] Connected to {addr}")

    tasks = [i for i in range(NUM_TASKS)]  # Список задач

    for task_data in tasks:
        try:
            # Отправляем задание клиенту
            conn.send(pickle.dumps(task_data))

            # Получаем результат
            result = pickle.loads(conn.recv(1024))
            print(f"[INFO] Result from {addr}: {result}")

        except Exception as e:
            print(f"[ERROR] Connection lost with {addr}: {e}")
            break

    # Сообщаем клиенту завершение работы
    conn.send(pickle.dumps(None))  # Отправляем `None` для остановки клиента
    conn.close()


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen()

        print(f"[INFO] Server listening on {SERVER_HOST}:{SERVER_PORT}")

        while True:
            # Ожидаем подключения клиента
            conn, addr = server_socket.accept()
            p = Process(target=handle_client, args=(conn, addr))
            p.start()


if __name__ == "__main__":
    server()
