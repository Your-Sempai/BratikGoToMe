from vk_api.keyboard import VkKeyboard, VkKeyboardColor


# Основное меню выбора фотографий
def Kemonomimi():
    keyboard = VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Некомими", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Кицунемими", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Инумими", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Усагимими ", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Картинки", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
    #  keyboard.add_line()#Обозначает добавление новой строки
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.NEGATIVE)

    #  keyboard.add_line()
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)
    #  keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()