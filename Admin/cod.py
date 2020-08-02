import random
from Connect.Connectbd import get_connection
from Admin.vkapi import vk, longpoll
from vk_api.bot_longpoll import VkBotEventType
from Admin.Add_Anime_bd import add_type_anime, add_studia_anime, add_status_anime
from Admin.Add_Anime_bd import add_janr_anime, add_box_text_anime, add_picture_anime, add_re_anime
from Admin.Add_Anime_bd import add_ep_anime, add_box_text_anime_two


def box(name):
    c = 0
    while True:
        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                mes = event.object.text.lower()
                mess = event.obj["text"]
                user_id = event.obj["peer_id"]
                text = mess
                if mes == 'всё':
                    vk.method("messages.send", {"peer_id": user_id, "message":
                        'Веди "Эпизодов (Кол-во серий)"',
                                                "random_id": random.randint(1, 2147483647)}
                          )
                    return
                elif c == 0:
                    add_box_text_anime(text, name)
                    c += 1
                else:
                    add_box_text_anime_two(text, name)


def add_anime_bd(name):
    while True:
        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                mes = event.object.text.lower()
                mess = event.obj["text"]
                user_id = event.obj["peer_id"]
                if 'тип' in mes.split()[:2]:
                    text = mess[4:]
                    add_type_anime(text, name)
                    vk.method("messages.send", {"peer_id": user_id, "message":
                                                'Введи "Статус (Завершено или выходит и т.д)"',
                                                "random_id": random.randint(1, 2147483647)}
                              )
                elif 'статус' in mes:
                    text = mess[7:]
                    print(text)
                    add_status_anime(text, name)
                    vk.method("messages.send", {"peer_id": user_id, "message":
                                                'Веди "Жанр (Жанры)"',
                                                "random_id": random.randint(1, 2147483647)}
                              )
                elif 'жанр' in mes:
                    text = mess[5:]
                    add_janr_anime(text, name)
                    vk.method("messages.send", {"peer_id": user_id, "message":
                                                'Веди "Рейтинг (R-13 или R-17 и т.д )"',
                                                "random_id": random.randint(1, 2147483647)}
                              )
                elif 'рейтинг' in mes:
                    text = mess[8:]
                    add_re_anime(text, name)
                    vk.method("messages.send", {"peer_id": user_id, "message":
                                                'Веди "Студия (Название студии)"',
                                                "random_id": random.randint(1, 2147483647)}
                              )
                elif 'студия' in mes:
                    text = mess[7:]
                    add_studia_anime(text, name)
                    vk.method("messages.send", {"peer_id": user_id, "message":
                                                'Веди "Описание"',
                                                "random_id": random.randint(1, 2147483647)}
                              )
                elif 'описание' in mes.split()[0]:
                    vk.method("messages.send", {"peer_id": user_id, "message":
                                                'Сенпай, Вводи описание по немного приблизительно по 40 слов'
                                                'Если описание кончилось, то напиши "Всё"',
                                                "random_id": random.randint(1, 2147483647)}
                              )
                    box(name)
                elif 'эпизодов' in mes:
                    text = mess[9:]
                    add_ep_anime(text, name)
                    vk.method("messages.send", {"peer_id": user_id, "message":
                                                'Веди "Фото (ссылка на фото(без vk.com))"',
                                                "random_id": random.randint(1, 2147483647)}
                              )
                elif 'фото' in mes:
                    text = mess[5:]
                    add_picture_anime(text, name)
                    vk.method("messages.send", {"peer_id": user_id, "message":
                        'Всё..Аниме добавлено, Сенпай',
                                                "random_id": random.randint(1, 2147483647)}
                              )
                    return


def name(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            if user_id == str:
                cursor.execute(f"SELECT * FROM account WHERE nik = {user_id}")
                return cursor.fetchone()[0]
            else:
                cursor.execute(f"SELECT * FROM account WHERE id = {user_id}")
                return cursor.fetchone()[0]
    finally:
        connection.close()


def dell_anibacks_money(user, count):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM account WHERE nik = '{user}'")
            row = cursor.fetchone()
            print(row)

            nam = row[2]
            num = row[3]
            print(nam, num)
            num -= int(count)
            print(nam)
            cursor.execute(f"UPDATE account SET money = '{num}' WHERE uid = {nam}")
            connection.commit()
    finally:
        connection.close()


def add_aniback_limit(user, count):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM account WHERE nik = '{user}'")
            row = cursor.fetchone()
            print(row)
            nam = row[2]
            num = row[3]
            print(nam, num)
            num += int(count)
            print(nam)
            cursor.execute(f"UPDATE account SET money = '{num}' WHERE uid    = {nam}")
            connection.commit()
    finally:
        connection.close()


def reset_limit():
    connction = get_connection()


def nik():
    count = random.randint(1, 99999)
    connction = get_connection()
    try:
        with connction.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM account WHERE nik={count}")
            if str(count) not in str(result):
                return f"user{count}"
    finally:
        connction.close()


def register(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM admins WHERE uid={user_id}")
            row = cursor.fetchone()
            if result != 0:
                return row
            else:
                cursor.execute(f"INSERT INTO admins(admin_name, uid) VALUES('{nik()}', {user_id})")
                connection.commit()
    finally:
        connection.close()


def add_tyan(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Тян'")
            row = cursor.fetchone()
            two = row[1] + ', ' + text
            cursor.execute(f"UPDATE Untitledd SET text = '{two}' WHERE name = 'Тян'")
            connection.commit()
    finally:
        connection.close()


def add_loli(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Лоли'")
            row = cursor.fetchone()
            two = row[1] + ', ' + text
            cursor.execute(f"UPDATE Untitledd SET text = '{two}' WHERE name = 'Лоли'")
            connection.commit()
    finally:
        connection.close()


def add_kyn(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Кун'")
            row = cursor.fetchone()
            two = row[1] + ', ' + text
            cursor.execute(f"UPDATE Untitledd SET text = '{two}' WHERE name = 'Кун'")
            connection.commit()
    finally:
        connection.close()


def add_oboi(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Обои'")
            row = cursor.fetchone()
            two = row[1] + ', ' + text
            cursor.execute(f"UPDATE Untitledd SET text = '{two}' WHERE name = 'Обои'")
            connection.commit()
    finally:
        connection.close()


def usagimimi(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Усагимими'")
            row = cursor.fetchone()
            two = row[1] + ', ' + text
            cursor.execute(f"UPDATE Untitledd SET text = '{two}' WHERE name = 'Усагимими'")
            connection.commit()
    finally:
        connection.close()


def nekomimi(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Некомими'")
            row = cursor.fetchone()
            two = row[1] + ', ' + text
            cursor.execute(f"UPDATE Untitledd SET text = '{two}' WHERE name = 'Некомими'")
            connection.commit()
    finally:
        connection.close()


def kitsunemimi(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Кицунемими'")
            row = cursor.fetchone()
            two = row[1] + ', ' + text
            cursor.execute(f"UPDATE Untitledd SET text = '{two}' WHERE name = 'Кицунемими'")
            connection.commit()
    finally:
        connection.close()


def inumimi(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Инумими'")
            row = cursor.fetchone()
            two = row[1] + ', ' + text
            cursor.execute(f"UPDATE Untitledd SET text = '{two}' WHERE name = 'Инумими'")
            connection.commit()
    finally:
        connection.close()


def check_animebd(name):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM Animebd WHERE Поиск = '{name}'")
            cursor.fetchone()
            if result == 1:
                return '1'
            else:
                return '0'
    finally:
        connection.close()