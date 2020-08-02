from vk_api.keyboard import VkKeyboard, VkKeyboardColor


# Профиль пользователя
def profil():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button("Профиль", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Просмотрено", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Запланировано", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Пересматриваю", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Смотрю", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Брошено", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()


# Аниме, которое пользователь просмотрел
def scanned_anime():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button("Профиль", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Запланировано", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Пересматриваю", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Смотрю", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Брошено", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()


# Аниме, которое пользователь запланировал
def planned_anime():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button("Профиль", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Просмотрено", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Пересматриваю", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Смотрю", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Брошено", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()


# Аниме, которое пользователь пересматривает
def review_anime():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button("Профиль", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Просмотрено", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Запланировано", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Смотрю", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Брошено", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()


# Аниме, которое пользователь смотрит
def look_anime():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button("Профиль", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Просмотрено", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Запланировано", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Пересматриваю", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Брошено", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()


# Аниме, которое пользователь бросил
def forsaken_anime():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button("Профиль", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Просмотрено", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Запланировано", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Пересматриваю", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Смотрю", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()
