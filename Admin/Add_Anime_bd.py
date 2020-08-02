from Connect.Connectbd import get_connection


def add_name_anime(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT COUNT(*) FROM Animebd")
            count = cursor.fetchone()
            print(count)
            count = int(count[0]) + 1
            print(count)
            cursor.execute(f"INSERT INTO Animebd(Названия, id) VALUES('{text}', '{count}')")
            connection.commit()
    finally:
        connection.close()


def add_type_anime(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()[0]
            cursor.execute(f"UPDATE Animebd SET type = '{text}' WHERE id = '{row}'")
            connection.commit()
    finally:
        connection.close()


def add_status_anime(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()[0]
            cursor.execute(f"UPDATE Animebd SET status = '{text}' WHERE id = '{row}'")
            connection.commit()
    finally:
        connection.close()


def add_janr_anime(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()[0]
            cursor.execute(f"UPDATE Animebd SET janr = '{text}' WHERE id = '{row}'")
            connection.commit()
    finally:
        connection.close()


def add_re_anime(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()[0]
            cursor.execute(f"UPDATE Animebd SET re = '{text}' WHERE id = '{row}'")
            connection.commit()
    finally:
        connection.close()


def add_studia_anime(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()[0]
            cursor.execute(f"UPDATE Animebd SET studio = '{text}' WHERE id = '{row}'")
            connection.commit()
    finally:
        connection.close()


def add_box_text_anime(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            print("+", text)
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()
            cursor.execute(f"UPDATE Animebd SET box_text = '{text}' WHERE id = '{row[0]}'")
            connection.commit()
    finally:
        connection.close()


def add_box_text_anime_two(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            print("+", text)
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()
            print(row)
            one = row[7] + '.' + text
            print(one)
            cursor.execute(f"UPDATE Animebd SET box_text = '{one}' WHERE id = '{row[0]}'")
            connection.commit()
    finally:
        connection.close()


def add_picture_anime(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()[0]
            cursor.execute(f"UPDATE Animebd SET picture = '{text}' WHERE id = '{row}'")
            connection.commit()
    finally:
        connection.close()


def add_video_anime(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()[0]
            cursor.execute(f"UPDATE Animebd SET video = '{text}' WHERE id = '{row}'")
            connection.commit()
    finally:
        connection.close()


def add_ep_anime(text, name):
    print(name)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd WHERE Названия = '{name}'")
            row = cursor.fetchone()[0]
            cursor.execute(f"UPDATE Animebd SET svaz = '{text}' WHERE id = '{row}'")
            connection.commit()
    finally:
        connection.close()
