from Connect.Connectbd import get_connection
import random


# Проверяет наличие пользователя в базе данных бота
# Если его нет, то регестрирует, если есть, то ничего не меняет
def check_player_to_in_the_bd(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM account WHERE uid={user_id}")
            id = cursor.fetchone()
            print(id)
            if user_id in id:
                return '1'
            else:
                return '0'

    finally:
        connection.close()


# Предоставляет пользователю его персональное ID в мире AnimeLib
def RanID():
    while True:
        count = random.randint(1, 999999)
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                result = cursor.execute(f"SELECT * FROM account WHERE id={count}")
                if count != result:
                    return count
        finally:
            connection.close()


# Предоставляет пользователю его персональный ник в мире AnimeLib
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


# Регестрирует пользователя в мире AnimeLib
def register(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM account WHERE uid={user_id}")
            row = cursor.fetchone()
            if result != 0:
                return '0'
            else:
                ni = nik()
                id = RanID()
                cursor.execute(f"INSERT INTO account(nik, uid, id) VALUES('{ni}', {user_id}, '{id}')")
                connection.commit()
                cursor.execute(f"SELECT * FROM account WHERE uid={user_id}")
                row = cursor.fetchone()
                cursor.execute(
                    f"INSERT INTO limitt(limit1, id, limit2, limit3, limit4, limit5, limit6, limit7) VALUES('0', {row[1]}, '0', '0', '0', '0', '0', '0')")
                connection.commit()
                cursor.execute(f"SELECT * FROM account WHERE uid={user_id}")
                row = cursor.fetchone()
                cursor.execute(
                    f"INSERT INTO UserAnime(id, pros_count, zap_count, pere_count, look_count, brosh_count) VALUES({row[1]}, '0', '0', '0', '0', '0')")
                connection.commit()
    finally:
        connection.close()


def set_name(user_id, name):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM account WHERE uid={user_id}")
            ro = cursor.fetchone()[1]

            cursor.execute(f"UPDATE account SET nik = '{name}' WHERE uid = {user_id}")
            connection.commit()

            cursor.execute(f"UPDATE limitt SET limit6 = '1' WHERE id = {ro}")
            connection.commit()

            cursor.execute(f"SELECT * FROM account WHERE uid={user_id}")
            row = cursor.fetchone()
            return row[0]

    finally:
        connection.close()


def limit_nik(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM limitt WHERE id={user_id}")
            row = cursor.fetchone()[6]
            if int(row) == 1:
                return '1'
            else:
                return '0'
    finally:
        connection.close()