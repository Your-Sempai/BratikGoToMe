from vk_api.keyboard import VkKeyboard, VkKeyboardColor


# Основное меню выбора фотографий
def foto():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Тян", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Лоли", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Кун", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Обои", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Кэмономими", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Меню", color=VkKeyboardColor.POSITIVE)

    #  keyboard.add_line()#Обозначает добавление новой строки
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()


# Тян
def tan():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Тян", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Картинки", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()#Обозначает добавление новой строки
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()


# Лоли
def loli():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Лоли", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Картинки", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()#Обозначает добавление новой строки
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()


# Куны
def kyn():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Кун", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Картинки", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()#Обозначает добавление новой строки
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()



def oboi():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Обои", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Картинки", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()#Обозначает добавление новой строки
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()
