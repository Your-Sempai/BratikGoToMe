import random
from Admin.vkapi import vk, longpoll
from vk_api.bot_longpoll import VkBotEventType
from Admin.cod import *
from Admin.Add_Anime_bd import *

for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:
        mes = event.object.text.lower()
        mess = event.obj["text"]
        peer_id = event.obj["peer_id"]
        #  Ответ на приветствие с ботом
        if mes == 'привет' or mes == 'хай':
            vk.method("messages.send", {"peer_id": peer_id, "message":
                                        'Привет',
                                        "random_id": random.randint(1, 2147483647)}
                      )

        elif mes.split()[0] == 'добавить':
            if len(mes) > 8:
                add_aniback_limit(mess.split()[1], mes.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            f"Сумма в размере {mes.split()[2]} Анибаксов, добавлена на аккаунт {mess.split()[1]}",
                                            "random_id": random.randint(1, 2147483647)}
                          )
            else:
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            "Ой..Видимо ты не правильно написал команду",
                                            "random_id": random.randint(1, 2147483647)}
                          )

        elif mes.split()[0] == 'убрать':
            if len(mes) > 6:
                dell_anibacks_money(mess.split()[1], mes.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            f"Сумма в размере {mes.split()[2]} Анибаксов, убрана с аккаунта {mess.split()[1]}",
                                            "random_id": random.randint(1, 2147483647)}
                         )

            else:
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            "Ой..Видимо ты не правильно написал команду",
                                            "random_id": random.randint(1, 2147483647)}
                          )

        elif mes.split()[0] == '+':
            if mes.split()[1] == 'тян':
                add_tyan(mess.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Ня, Добавлено~',
                                            "random_id": random.randint(1, 2147483647)}
                          )
            elif mes.split()[1] == 'лоли':
                add_loli(mess.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Ня, Добавлено~',
                                            "random_id": random.randint(1, 2147483647)}
                          )
            elif mes.split()[1] == 'кун':
                add_kyn(mess.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Ня, Добавлено~',
                                            "random_id": random.randint(1, 2147483647)}
                          )
            elif mes.split()[1] == 'обои':
                add_oboi(mess.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Ня, Добавлено~',
                                            "random_id": random.randint(1, 2147483647)}
                         )
            elif mes.split()[1] == 'усагимими':
                usagimimi(mess.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Ня, Добавлено~',
                                            "random_id": random.randint(1, 2147483647)}
                         )
            elif mes.split()[1] == 'некомими':
                nekomimi(mess.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Ня, Добавлено~',
                                            "random_id": random.randint(1, 2147483647)}
                         )
            elif mes.split()[1] == 'кицунемими':
                kitsunemimi(mess.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Ня, Добавлено~',
                                            "random_id": random.randint(1, 2147483647)}
                         )
            elif mes.split()[1] == 'инумими':
                inumimi(mess.split()[2])
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Ня, Добавлено~',
                                            "random_id": random.randint(1, 2147483647)}
                         )
            elif mes.split()[1] == 'аниме':
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                'Веди название Аниме',
                                "random_id": random.randint(1, 2147483647)}
              )
        elif mes == 'аниме':
            vk.method("messages.send", {"peer_id": peer_id, "message":
                                        'Сенпай, чтобы добавить аниме в список\n'
                                        'Введи "Название (Название аниме)"',
                                        "random_id": random.randint(1, 2147483647)}
                      )
        elif 'название' in mes.split()[:7]:
            name = mess[9:]
            one = check_animebd(name)
            if one == '1':
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Сенпай, это аниме уже есть в базе данных',
                                            "random_id": random.randint(1, 2147483647)}
                          )
            else:
                print(name)
                add_name_anime(name)
                vk.method("messages.send", {"peer_id": peer_id, "message":
                                            'Введи "Тип (ТВ сериаал или фильм и т.д)"',
                                            "random_id": random.randint(1, 2147483647)}
                          )
                add_anime_bd(name)
