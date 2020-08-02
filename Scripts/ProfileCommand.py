from Connect.Connectbd import *


# Проверяет информацию о пользователе
def profile(peer_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM account WHERE uid={peer_id}")
            row = cursor.fetchone()
            print(row)
            if result == 1:
                return row
    finally:
        connection.close()


def count_anime(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM UserAnime WHERE id={user_id}")
            row = cursor.fetchone()
            return row
    finally:
        connection.close()


def check(text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Animebd")
            row = cursor.fetchone()[10]
            print(str(row).split(', '))
            if text in str(row).split(', '):
                cursor.execute(f"SELECT * FROM Animebd")
                row = cursor.fetchone()[1]
                print(row)
                return row
            else:
                return '0'
    finally:
        connection.close()


# Добавляет аниме пользователя в базу данных бота(после проверки check())
# Работает вместе с add_pros_anime()
def get_anime(anime, user_progress, id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            if 'просмотрено' in user_progress:
                cursor.execute(f"SELECT * FROM limitt WHERE id = '{id}'")
                limit = cursor.fetchone()[1]
                print(limit)
                print(anime)
                if limit == 0:
                    cursor.execute(f"SELECT pros_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT pros FROM UserAnime WHERE id = '{id}'")
                    pros = cursor.fetchone()

                    cursor.execute(f"UPDATE UserAnime SET pros = '{anime}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET pros_count = '{count}' WHERE id = '{id}'")
                    connection.commit()

                    cursor.execute(f"UPDATE limitt SET limit1 = '1' WHERE id = '{id}'")
                    connection.commit()
                else:
                    cursor.execute(f"SELECT pros_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT pros FROM UserAnime WHERE id = '{id}'")
                    pros = cursor.fetchone()

                    pros = str(*pros) + ', ' + anime

                    cursor.execute(f"UPDATE UserAnime SET pros = '{pros}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET pros_count = '{count}' WHERE id = '{id}'")
                    connection.commit()
            elif 'брошено' in user_progress:
                cursor.execute(f"SELECT * FROM limitt WHERE id = '{id}'")
                limit = cursor.fetchone()[2]
                print(limit)
                print(anime)
                if limit == 0:
                    cursor.execute(f"SELECT brosh_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT brosh FROM UserAnime WHERE id = '{id}'")
                    pros = cursor.fetchone()

                    cursor.execute(f"UPDATE UserAnime SET brosh = '{anime}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET brosh_count = '{count}' WHERE id = '{id}'")
                    connection.commit()

                    cursor.execute(f"UPDATE limitt SET limit2 = '1' WHERE id = '{id}'")
                    connection.commit()
                else:
                    cursor.execute(f"SELECT brosh_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT brosh FROM UserAnime WHERE id = '{id}'")
                    pros = cursor.fetchone()

                    pros = str(*pros) + ', ' + anime

                    cursor.execute(f"UPDATE UserAnime SET brosh = '{pros}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET brosh_count = '{count}' WHERE id = '{id}'")
                    connection.commit()
            elif 'запланировано' in user_progress:
                cursor.execute(f"SELECT * FROM limitt WHERE id = '{id}'")
                limit = cursor.fetchone()[3]
                print(limit)
                print(anime)
                if limit == 0:
                    cursor.execute(f"SELECT zap_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT zap FROM UserAnime WHERE id = '{id}'")
                    pros = cursor.fetchone()

                    cursor.execute(f"UPDATE UserAnime SET zap = '{anime}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET zap_count = '{count}' WHERE id = '{id}'")
                    connection.commit()

                    cursor.execute(f"UPDATE limitt SET limit3 = '1' WHERE id = '{id}'")
                    connection.commit()
                else:
                    cursor.execute(f"SELECT zap_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT zap FROM UserAnime WHERE id = '{id}'")
                    pros = cursor.fetchone()

                    pros = str(*pros) + ', ' + anime

                    cursor.execute(f"UPDATE UserAnime SET zap = '{pros}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET zap_count = '{count}' WHERE id = '{id}'")
                    connection.commit()
            elif 'смотрю' in user_progress:
                cursor.execute(f"SELECT * FROM limitt WHERE id = '{id}'")
                limit = cursor.fetchone()[4]
                print(limit)
                print(anime)
                if limit == 0:
                    cursor.execute(f"SELECT look_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT look FROM UserAnime WHERE id = '{id}'")
                    cursor.fetchone()

                    cursor.execute(f"UPDATE UserAnime SET look = '{anime}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET look_count = '{count}' WHERE id = '{id}'")
                    connection.commit()

                    cursor.execute(f"UPDATE limitt SET limit4 = '1' WHERE id = '{id}'")
                    connection.commit()
                else:
                    cursor.execute(f"SELECT look_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT look FROM UserAnime WHERE id = '{id}'")
                    pros = cursor.fetchone()

                    pros = str(*pros) + ', ' + anime

                    cursor.execute(f"UPDATE UserAnime SET look = '{pros}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET look_count = '{count}' WHERE id = '{id}'")
                    connection.commit()
            elif 'пересматриваю' in user_progress:
                cursor.execute(f"SELECT * FROM limitt WHERE id = '{id}'")
                limit = cursor.fetchone()[5]
                print(limit)
                print(anime)
                if limit == 0:
                    cursor.execute(f"SELECT pere_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT pere FROM UserAnime WHERE id = '{id}'")
                    pros = cursor.fetchone()

                    cursor.execute(f"UPDATE UserAnime SET pere = '{anime}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET pere_count = '{count}' WHERE id = '{id}'")
                    connection.commit()

                    cursor.execute(f"UPDATE limitt SET limit5 = '1' WHERE id = '{id}'")
                    connection.commit()
                else:
                    cursor.execute(f"SELECT pere_count FROM UserAnime WHERE id = '{id}'")
                    num = cursor.fetchone()
                    count = int(*num) + 1

                    cursor.execute(f"SELECT pere FROM anime WHERE id = '{id}'")
                    pros = cursor.fetchone()

                    pros = str(*pros) + ', ' + anime

                    cursor.execute(f"UPDATE UserAnime SET pere = '{pros}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET pere_count = '{count}' WHERE id = '{id}'")
                    connection.commit()
    finally:
        connection.close()


# Проверяет, нет ли в данных пользователя аниме которое он хочет добавить
# Работает вместе с get_anime()
def add_pros_anime(anime, uid, user_progress):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM account WHERE uid = '{uid}'")
            id = cursor.fetchone()[1]
            print('+')
            anim = False
            cursor.execute(f"SELECT * FROM UserAnime WHERE id = '{id}'")
            a = cursor.fetchone()
            print(a)
            if anime in str(a):
                print('++')
                anim = True
            print(anim)

            if anim:
                cursor.execute(f"SELECT pros FROM UserAnime WHERE id = '{id}'")
                pros = cursor.fetchone()
                if anime in str(pros):
                    print('good')
                    print(pros)
                    one = str(*pros).split(', ')
                    print(one)
                    count = 0
                    for i in range(len(one)):
                        if anime in one[i]:
                            count = i
                    del one[count]
                    print(one)
                    cursor.execute(f"SELECT pros_count FROM UserAnime WHERE id = '{id}'")
                    a = cursor.fetchone()
                    a = int(*a) - 1
                    cursor.execute(f"UPDATE UserAnime SET pros = '{', '.join(one)}' WHERE id = '{id}'")
                    connection.commit()
                    cursor.execute(f"UPDATE UserAnime SET pros_count = '{a}' WHERE id = '{id}'")
                    connection.commit()
                    get_anime(anime, user_progress, id)
                else:
                    cursor.execute(f"SELECT brosh FROM UserAnime WHERE id = '{id}'")
                    brosh = cursor.fetchone()
                    if anime in str(brosh):
                        print('good')
                        one = str(*brosh).split(', ')
                        print(one)
                        count = 0
                        for i in range(len(one)):
                            if anime in one[i]:
                                count = i
                        del one[count]
                        print(one)
                        cursor.execute(f"SELECT brosh_count FROM UserAnime WHERE id = '{id}'")
                        a = cursor.fetchone()
                        a = int(*a) - 1
                        cursor.execute(f"UPDATE UserAnime SET brosh = '{', '.join(one)}' WHERE id = '{id}'")
                        connection.commit()
                        cursor.execute(f"UPDATE UserAnime SET brosh_count = '{a}' WHERE id = '{id}'")
                        connection.commit()
                        get_anime(anime, user_progress, id)
                    else:
                        cursor.execute(f"SELECT look FROM UserAnime WHERE id = '{id}'")
                        look = cursor.fetchone()
                        if anime in str(look):
                            print('good')
                            one = str(*look).split(', ')
                            print(one)
                            count = 0
                            for i in range(len(one)):
                                if anime in one[i]:
                                    count = i
                            del one[count]
                            print(one)
                            cursor.execute(f"SELECT look_count FROM UserAnime WHERE id = '{id}'")
                            a = cursor.fetchone()
                            a = int(*a) - 1
                            cursor.execute(f"UPDATE UserAnime SET look = '{', '.join(one)}' WHERE id = '{id}'")
                            connection.commit()
                            cursor.execute(f"UPDATE UserAnime SET look_count = '{a}' WHERE id = '{id}'")
                            connection.commit()
                            get_anime(anime, user_progress, id)
                        else:
                            cursor.execute(f"SELECT pere FROM UserAnime WHERE id = '{id}'")
                            pere = cursor.fetchone()
                            if anime in str(pere):
                                print('good')
                                one = str(*pere).split(', ')
                                print(one)
                                count = 0
                                for i in range(len(one)):
                                    if anime in one[i]:
                                        count = i
                                del one[count]
                                print(one)
                                cursor.execute(f"SELECT pere_count FROM UserAnime WHERE id = '{id}'")
                                a = cursor.fetchone()
                                a = int(*a) - 1
                                cursor.execute(f"UPDATE UserAnime SET pere = '{', '.join(one)}' WHERE id = '{id}'")
                                connection.commit()
                                cursor.execute(f"UPDATE UserAnime SET pere_count = '{a}' WHERE id = '{id}'")
                                connection.commit()
                                get_anime(anime, user_progress, id)
                            else:
                                cursor.execute(f"SELECT zap FROM UserAnime WHERE id = '{id}'")
                                zap = cursor.fetchone()
                                if anime in str(zap):
                                    print('good')
                                    one = str(*zap).split(', ')
                                    print(one)
                                    count = 0
                                    for i in range(len(one)):
                                        if anime in one[i]:
                                            count = i
                                    del one[count]
                                    print(one)
                                    cursor.execute(f"SELECT zap_count FROM UserAnime WHERE id = '{id}'")
                                    a = cursor.fetchone()
                                    a = int(*a) - 1
                                    cursor.execute(f"UPDATE UserAnime SET zap = '{', '.join(one)}' WHERE id = '{id}'")
                                    connection.commit()
                                    cursor.execute(f"UPDATE UserAnime SET zap_count = '{a}' WHERE id = '{id}'")
                                    connection.commit()
                                    get_anime(anime, user_progress, id)
                                else:
                                    get_anime(anime, user_progress, id)
            else:
                get_anime(anime, user_progress, id)
    finally:
        connection.close()


# Берёт из базы данных бота список аниме пользователя и отправляет ему
def spisok_anime(user_id, message):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM account WHERE uid = {user_id}")
            id = cursor.fetchone()[1]
            if message == 'просмотрено':
                cursor.execute(f"SELECT pros FROM UserAnime WHERE id = {id}")
                anime = cursor.fetchone()
                if anime[0] == '' or None in anime:
                    return 'Пусто'
                else:
                    return anime
            if message == 'запланировано':
                cursor.execute(f"SELECT zap FROM UserAnime WHERE id = {id}")
                anime = cursor.fetchone()
                if anime[0] == '' or None in anime:
                    return 'Пусто'
                else:
                    return anime
            if message == 'смотрю':
                cursor.execute(f"SELECT look FROM UserAnime WHERE id = {id}")
                anime = cursor.fetchone()
                print(anime)
                if anime[0] == '' or None in anime:
                    return 'Пусто'
                else:
                    return anime
            if message == 'пересматриваю':
                cursor.execute(f"SELECT pere FROM UserAnime WHERE id = {id}")
                anime = cursor.fetchone()
                if anime[0] == '' or None in anime:
                    return 'Пусто'
                else:
                    return anime
            if message == 'брошено':
                cursor.execute(f"SELECT brosh FROM UserAnime WHERE id = {id}")
                anime = cursor.fetchone()
                print(anime)
                if anime == '' or None in anime:
                    return 'Пусто'
                else:
                    return anime

    finally:
        connection.close()


# По списку просмотренных аниме дарует пользователю титул
def level(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT lvl FROM account WHERE uid={user_id}")
            lvl = cursor.fetchone()
            rows = str(lvl).split(',')
            row2 = str(rows[0]).split('(')
            row = int(str(row2[1]))
            if row == 1:
                return "1"
            else:
                return "0"
    finally:
        connection.close()


def check_count_pros_anime(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT pros_count FROM UserAnime WHERE id={user_id}")
            counts = cursor.fetchone()
            count = int(*counts)
            print(int(*counts))
            if count >= 10 and count < 60:
                return '1'
            elif count >= 60 and count < 100:
                return '2'
            elif count >= 100 and count < 145:
                return '3'
            elif count >= 145 and count < 200:
                return '4'
            elif count >= 200 and count < 310:
                return '5'
            elif count >= 310 and count < 400:
                return '6'
            elif count >= 400 and count < 550:
                return '7'
            elif count >= 550 and count < 666:
                return '8'
            elif count >= 666 and count < 750:
                return '9'
            elif count >= 750 and count < 777:
                return '10'
            elif count >= 777 and count < 900:
                return '11'
            elif count >= 900 and count < 1000:
                return '12'
            elif count >= 1000 and count < 1234:
                return '13'
            elif count >= 1234 and count < 1500:
                return '14'
            elif count >= 1500 and count < 2000:
                return '15'
            elif count >= 2000 and count < 2020:
                return '16'
            elif count >= 2020 and count < 2600:
                return '17'
            elif count >= 2600 and count < 3500:
                return '18'
            elif count >= 3500 and count < 5000:
                return '19'
            elif count >= 5000 and count < 7000:
                return '20'
            elif count >= 7000 and count < 10000:
                return '21'
            elif count >= 10000:
                return '22'
    finally:
        connection.close()