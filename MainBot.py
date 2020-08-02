from random import randint
from Connect.vkapi import vk, longpoll
from vk_api.bot_longpoll import VkBotEventType
from Keyboard.ProfilKeyboard import *
from Keyboard.MainKeyboard import *
from Scripts.ProfileCommand import *
from Scripts.RegisterCommand import *
from Scripts.AnimeShow import *
from Keyboard.AnimeShowKeyboard import *
from Scripts.ImageCommand import *
from Keyboard.ImageKeyboard import *
from Keyboard.yshik import *

print("~")

while True:
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            mess = event.obj['text']  # Сообщение пользователя
            mes = event.object.text.lower()  # Сообщение пользователя(маленькая буква)
            peer_id = event.obj["peer_id"]  # ID пользователя

            if mes == 'профиль':
                keyboard = profil()
                one = profile(peer_id)
                print(one)
                count = count_anime(peer_id)
                lvl = level(peer_id)
                if lvl == "0":
                    vk.method("messages.send", {"peer_id": peer_id, "message":
                            f"♡♡Привет, {one[0]}♡♡\n"
                            f"ღღТвой ID: {one[2]}ღღ\n"
                            f"★★Анибаксы: {one[3]}★★\n"
                            "       ★★Аниме★★       \n"
                            f'★★Просмотрено: {count[2]}★★\n'
                            f'★★Запланировано: {count[4]}★★\n'
                            f'★★Смотрю: {count[8]}★★\n'
                            f'★★Брошено: {count[10]}★★\n'
                            f'★★Пересматриваю: {count[6]}★★\n'
                            f''
                            ,
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                else:

                    vk.method("messages.send", {"peer_id": peer_id, "message":
                                f"♡♡Привет, {one[0]}♡♡\n"
                                f"ღღТвой ID: {one[2]}ღღ\n"
                                f"★★Анибаксы: {one[3]}★★\n"
                                f'††     Админ     ††\n'
                                "   ★★  Аниме   ★★   \n"
                                f'★★Просмотрено: {count[2]}★★\n'
                                f'★★Запланировано: {count[4]}★★\n'
                                f'★★Смотрю: {count[8]}★★\n'
                                f'★★Брошено: {count[10]}★★\n'
                                f'★★Пересматриваю: {count[6]}★★\n'
                                f''
                                ,
                                                        "keyboard": keyboard,
                                                        "random_id": random.randint(1, 2147483647)})

            elif mes == 'меню':
                keyboard = main_keyboard()
                if register(peer_id) == '0':
                    vk.method("messages.send", {"peer_id": peer_id,
                                                "message":
                                                    f"С возвращением, Братик~\n",
                                                "keyboard": keyboard,
                                                "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": peer_id,
                                                "message":
                                                    f"Добро пожаловать, Братик~\n",
                                                "keyboard": keyboard,
                                                "random_id": random.randint(1, 2147483647)})
            elif 'просмотрено' in mes.split()[0]:
                keyboard = scanned_anime()
                if len(mes) > 11:
                    one = check(mess[12:])
                    name = mess[12:]
                    if one == '0':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Сенпай, Такое Аниме я ещё пока не знаю\n"
                                                        f"Подожди пока я изучу это аниме\n"
                                                        f"Это происходит быстро~",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": 557056639,
                                                    "message":
                                                        f"Хозяин, {peer_id}, Хотел добавить в свой список это Аниме:\n"
                                                        f"{mess[12:]}",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        add_pros_anime(one, peer_id, mes.split()[:12])
                        print(mes.split()[0])
                        vk.method("messages.send", {"peer_id": peer_id, "message":
                            f"Добавлено",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                else:
                    one = spisok_anime(peer_id, mes)
                    if one == 'Пусто':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Пусто",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"{', '.join(one)}\n",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
            elif 'брошено' in mes.split()[0]:
                keyboard = forsaken_anime()
                if len(mes) > 7:
                    one = check(mess[8:])
                    name = mess[8:]
                    print(name)
                    if one == '0':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Сенпай, Такое Аниме я ещё пока не знаю\n"
                                                        f"Подожди пока я изучу это аниме\n"
                                                        f"Это происходит быстро~",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": 557056639,
                                                    "message":
                                                        f"Хозяин, {peer_id}, Хотел добавить в свой список это Аниме:\n"
                                                        f"{mess[12:]}",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        add_pros_anime(one, peer_id, mes.split()[:8])
                        print(mes.split()[0])
                        vk.method("messages.send", {"peer_id": peer_id, "message":
                            f"Добавлено",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                else:
                    one = spisok_anime(peer_id, mes)
                    print(one)
                    if one == 'Пусто':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Пусто",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"{one}\n",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2137483647)})
            elif 'запланировано' in mes.split()[0]:
                keyboard = planned_anime()
                if len(mes) > 13:
                    one = check(mess[14:])
                    name = mess[14:]
                    if one == '0':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Сенпай, Такое Аниме я ещё пока не знаю\n"
                                                        f"Подожди пока я изучу это аниме\n"
                                                        f"Это происходит быстро~",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": 557056639,
                                                    "message":
                                                        f"Хозяин, {peer_id}, Хотел добавить в свой список это Аниме:\n"
                                                        f"{mess[12:]}",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        add_pros_anime(one, peer_id, mes.split()[:14])
                        print(mes.split()[0])
                        vk.method("messages.send", {"peer_id": peer_id, "message":
                            f"Добавлено",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                else:
                    one = spisok_anime(peer_id, mes)
                    if one == 'Пусто':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Пусто",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"{', '.join(one)}\n",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                # Пользователь устанавливает себе имя
            elif 'смотрю' in mes.split()[0]:
                keyboard = look_anime()
                if len(mes) > 6:
                    one = check(mess[7:])
                    name = mess[7:]
                    if one == '0':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Сенпай, Такое Аниме я ещё пока не знаю\n"
                                                        f"Подожди пока я изучу это аниме\n"
                                                        f"Это происходит быстро~",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": 557056639,
                                                    "message":
                                                        f"Хозяин, {peer_id}, Хотел добавить в свой список это Аниме:\n"
                                                        f"{mess[12:]}",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        add_pros_anime(name, peer_id, mes.split()[:7])
                        print(mes.split()[0])
                        vk.method("messages.send", {"peer_id": peer_id, "message":
                            f"Добавлено",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                else:
                    one = spisok_anime(peer_id, mes)
                    if one == 'Пусто':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Пусто",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"{', '.join(one)}\n",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
            elif 'пересматриваю' in mes.split()[0]:
                keyboard = review_anime()
                if len(mes) > 13:
                    one = check(mess[14:])
                    name = mess[14:]
                    if one == '0':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Сенпай, Такое Аниме я ещё пока не знаю\n"
                                                        f"Подожди пока я изучу это аниме\n"
                                                        f"Это происходит быстро~",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": 557056639,
                                                    "message":
                                                        f"Хозяин, {peer_id}, Хотел добавить в свой список это Аниме:\n"
                                                        f"{mess[12:]}",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        add_pros_anime(name, peer_id, mes.split()[:14])
                        print(mes.split()[0])
                        vk.method("messages.send", {"peer_id": peer_id, "message":
                            f"Добавлено",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                else:
                    one = spisok_anime(peer_id, mes)
                    if one == 'Пусто':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Пусто",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"{', '.join(one)}\n",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
            elif 'имя' in mes:
                print(mess[4:])
                name = mess[4:]
                keyboard = main_keyboard()
                if limit_nik(peer_id) == '0':
                    vk.method("messages.send", {"peer_id": peer_id, "message":
                                                f"Воу-Воу, теперь ты {set_name(peer_id, name)}",
                                                "keyboard": keyboard,
                                                "random_id": random.randint(1, 2147483647)})

                else:
                    vk.method("messages.send", {"peer_id": peer_id, "message":
                                                f"Прости, Братик, но ты не можешь сменить ник\n"
                                                f"Купи карточку смены ника",
                                                "keyboard": keyboard,
                                                "random_id": random.randint(1, 2147483647)})
            elif mes == 'аниме':
                keyboard = anime()
                vk.method("messages.send", {"peer_id": peer_id,
                                            "message":
                                                f"Нажми на 'Рандом', чтобы увидеть аниме\n",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'рандом':
                keyboard = anime()
                count = Anime()
                one = ran_anime(count)
                print(one)
                vk.method("messages.send", {"peer_id": peer_id,
                                            "attachment": one[8],
                                            "message":
                                                f"{one[1]}\n"
                                                "\n"
                                                f"Тип: {one[2]}\n"
                                                f"Эпизодов: {one[9]}\n"
                                                f"Статус: {one[3]}\n"
                                                f"Жанры: {one[4]}\n"
                                                f"Рейтинг: {one[5]}\n"
                                                f"Студия: {one[6]}\n"
                                                f"\n"
                                                f"Описание:\n"
                                                "\n"
                                                f"{one[7]}\n",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'тян':
                keyboard = tan()
                vk.method("messages.send", {"peer_id": peer_id, "attachment": tyan(),
                                            "message":
                                                f"Ня~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'кун':
                keyboard = kyn()
                vk.method("messages.send", {"peer_id": peer_id, "attachment": kyn2(),
                                            "message":
                                                f"Ня~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'лоли':
                keyboard = loli()
                vk.method("messages.send", {"peer_id": peer_id, "attachment": lol(),
                                            "message":
                                                f"Ня~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'обои':
                keyboard = oboi()
                vk.method("messages.send", {"peer_id": peer_id, "attachment": obo(),
                                            "message":
                                                f"Ня~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'кэмономими':
                keyboard = Kemonomimi()
                vk.method("messages.send", {"peer_id": peer_id,
                                            "message":
                                                f"Ня~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'усагимими':
                keyboard = Kemonomimi()
                vk.method("messages.send", {"peer_id": peer_id, "attachment": usagimimi(),
                                            "message":
                                                f"Ня~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'некомими':
                keyboard = Kemonomimi()
                vk.method("messages.send", {"peer_id": peer_id, "attachment": nekomimi(),
                                            "message":
                                                f"Ня~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'кицунемими':
                keyboard = Kemonomimi()
                vk.method("messages.send", {"peer_id": peer_id, "attachment": kitsunemimi(),
                                            "message":
                                                f"Ня~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'инумими':
                keyboard = Kemonomimi()
                vk.method("messages.send", {"peer_id": peer_id, "attachment": inumimi(),
                                            "message":
                                                f"Ня~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'картинки':
                keyboard = foto()
                vk.method("messages.send", {"peer_id": peer_id,
                                            "message":
                                                f"Выбирай, Братик~",
                                            "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif mes == 'магазин':
                keyboard = shop()
                vk.method("messages.send", {"peer_id": peer_id,
                                                "message":
                                                    f"Прости, Братик, но магазин пока не работает:<\n",
                                                "keyboard": keyboard,
                                                "random_id": random.randint(1, 2147483647)})
            else:
                if check_player_to_in_the_bd(peer_id) == '1':
                    register(peer_id)
                    id = 0
                    keyboard = main_keyboard()
                    one = check_anime(mess)
                    if one.split(', ')[0] == '0':
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"Сенпай, Такое Аниме я ещё пока не знаю\n"
                                                        f"Но если ты ввёл что-то другое, то не надо так",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": 557056639,
                                                    "message":
                                                        f"Один Братик ввёл неизвестное мне\n"
                                                        f"{mess}",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        id = one.split(', ')[1]
                        two = a(id)
                        vk.method("messages.send", {"peer_id": peer_id,
                                                    "message":
                                                        f"{two[1]}\n"
                                                        "\n"
                                                        f"Тип: {two[2]}\n"
                                                        f"Эпизодов: {two[9]}\n"
                                                        f"Статус: {two[3]}\n"
                                                        f"Жанры: {two[4]}\n"
                                                        f"Рейтинг: {two[5]}\n"
                                                        f"Студия: {two[6]}\n"
                                                        f"\n"
                                                        f"Описание:\n"
                                                        "\n"
                                                        f"{two[7]}\n",
                                                    "keyboard": keyboard,
                                                    "random_id": random.randint(1, 2147483647)})
                else:
                    register(peer_id)
                    keyboard = main_keyboard()
                    vk.method("messages.send", {"peer_id": peer_id,
                                                "message":
                                                    f"Добро пожаловать, Сенпай\n",
                                                "keyboard": keyboard,
                                                "random_id": random.randint(1, 2147483647)})