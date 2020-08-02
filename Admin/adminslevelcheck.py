from ScriptsVkBot.Connectbd import get_connection
import random
from Admin.vkapi import vk


def bd():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            nik = 'user85373'
            cursor.execute(f"SELECT * FROM account WHERE nik = '{nik}'")
            row = cursor.fetchone()
            if row == None:
                return 'Никого нет'
            else:
                return row
    finally:
        connection.close()


def command(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM account WHERE uid = {user_id}")
            row = cursor.fetchone()
            if row[2] == '0':
                vk.method("messages.send", {"peer_id": user_id, "message":
                                            f"Привет, {row[0]}"
                                            f"Вот твои команды:",
                                            "random_id": random.randint(1, 2147483647)}
                          )
                return
            elif row[2] == '10':
                vk.method("messages.send", {"peer_id": user_id, "message":
                                            f"{row[0]}~"
                                            f"Вот твои команды:",
                                            "random_id": random.randint(1, 2147483647)}
                          )
                return
    finally:
        connection.close()

def chek_level_admin(command, user_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM admins WHERE uid = {user_id}")
        row = cursor.fetchone()
        if command == 'добавить' or command == 'убрать':
            if row[2] == '0':
                return False
            else:
                return True
        else:
            return