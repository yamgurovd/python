"""
Вам дан словарь user_database с именами пользователей и их паролями. Допишите функцию check_user так,
чтобы она по логину пользователя проверяла, существует он или нет, после чего с помощью вложенного
условия проверяла правильность пароля этого пользователя.

Функция должна возвращать только True или False.

Примечание: чтобы вернуть True, напишите "return True"; чтобы вернуть False, напишите "return False".
"""

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

user_name = 'user,jjnjn'

for i in user_database:
    if user_name in user_database:
        print(f'{i}: {user_database[i]}')

def check_user(username: str,
               passwowrd: str) -> bool:

    if username in user_database:

        if passwowrd == user_database[username]:
            return True
        else:
            return False
    return False


d = check_user(username="username", passwowrd="password")

# print(d)