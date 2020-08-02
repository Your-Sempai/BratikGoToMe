from vk_api.keyboard import VkKeyboard, VkKeyboardColor


# Основное меню
def main_keyboard():
    keyboard = VkKeyboard(one_time=False)
    #False Если клавиатура должна оставаться откртой после нажатия на кнопку
    #True если она должна закрваться

    keyboard.add_button("Картинки", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Профиль", color=VkKeyboardColor.POSITIVE)

    keyboard.add_button("Магазин", color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button('Аниме', color=VkKeyboardColor.POSITIVE)

    #  keyboard.add_line()#Обозначает добавление новой строки
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()


def shop():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()#Обозначает добавление новой строки
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()