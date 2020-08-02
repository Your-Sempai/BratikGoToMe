from Connect.Connectbd import get_connection
import random


# Кол-во аниме в базе данных
def Anime():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT COUNT(*) FROM Animebd")
            return cursor.fetchone()[0]
    finally:
        connection.close()


# Рандомное аниме когда пользователь нажмёт на "Рандом"
def ran_anime(count):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            ran = random.randint(1, int(count))
            cursor.execute(f"SELECT * FROM Animebd WHERE id = '{ran}'")
            row = cursor.fetchone()
            return row
    finally:
        connection.close()


# Проверяет аниме в базе данных
def check_anime(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            result = cursor.execute(f"SELECT COUNT(id) FROM Animebd")
            row = cursor.fetchone()
            print(result)
            print(*row)
            for i in range(int(*row)):
                print(i)
                cursor.execute(f"SELECT Поиск FROM Animebd WHERE id = {i + 1}")
                anim = cursor.fetchone()
                print(anim)
                if text in str(anim).split(', '):
                    return f"1, {i}"
            return '0'
    finally:
        connection.close()


# Отправляет пользователю информацию по аниме которое он ввёл если это аниме есть в базе данных
def check_two(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM Animebd WHERE Поиск = '{text}'")
            row = cursor.fetchone()
            print(row)
            if result == 1:
                return row
            else:
                return '0'
    finally:
        connection.close()


def a(id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd WHERE id = '{int(id) + 1}'")
            row = cursor.fetchone()
            return row
    finally:
        connection.close()
