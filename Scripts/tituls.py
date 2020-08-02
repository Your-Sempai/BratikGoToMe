from Connect.Connectbd import get_connection


def id_admin(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Senpai"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_new(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Начинающий"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_1(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Добро пожаловать"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_2(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Тлько начало"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_3(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "+Знания"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_4(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Сама беззаботность"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_5(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Фанатик"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_6(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Знающий"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_7(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Хвастун"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_8(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Безработный?"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_9(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Сатана?"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_10(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Кхм..не запланированнный титул"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_11(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "До конца далеко"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_12(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Бесконечность не предел"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_13(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Пути назад нет"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_14(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Один, два, три, четыре.. сколько?"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_15(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Анимешник"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_16(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Ты живое?"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_17(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Корона?"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_18(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Новый герой?"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_19(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Отаку"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_20(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Святейший"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_21(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "Гений"
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()


def id_22(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            name_titul = "ERROR.."
            cursor.execute(f"SELECT name_titul FROM Titul WHERE id={user_id}")
            tituls = cursor.fetchone()
            if name_titul not in str(*tituls):
                if tituls != None:
                    tit = str(*tituls) + ', ' + name_titul
                    print(tit)
                    cursor.execute(f"UPDATE Titul SET name_titul = '{tit}' WHERE id = {user_id}")
                    connection.commit()
                else:
                    cursor.execute(f"UPDATE Titul SET name_titul = '{name_titul}' WHERE id = {user_id}")
                    connection.commit()
            else:
                return '0'
    finally:
        connection.close()