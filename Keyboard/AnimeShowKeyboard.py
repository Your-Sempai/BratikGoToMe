from vk_api.keyboard import VkKeyboard, VkKeyboardColor


# Клавиатура после вызова меню показа аниме
def anime():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button("Рандом", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)

    # keyboard.add_line()
    # keyboard.add_button("Комедия ", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("История ", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Драма ", color=VkKeyboardColor.POSITIVE)

    # keyboard.add_line()
    # keyboard.add_button("Научная фантастика", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Военные", color=VkKeyboardColor.POSITIVE)

    # keyboard.add_line()
    # keyboard.add_button("Меха", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Сэнтай", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Спокон ", color=VkKeyboardColor.POSITIVE)

    # keyboard.add_line()
    # keyboard.add_button("Киберпанк", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Паропанк", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Фэнтези", color=VkKeyboardColor.POSITIVE)

    # keyboard.add_line()
    # keyboard.add_button("Мистика", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Парапсихология", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Апокалиптика", color=VkKeyboardColor.POSITIVE)

    # keyboard.add_line()
    # keyboard.add_button("Романтика", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Повседневность", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Боевик", color=VkKeyboardColor.POSITIVE)

    # keyboard.add_line()
    # keyboard.add_button("Детектив", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Отаку", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Хентай", color=VkKeyboardColor.POSITIVE)

    # keyboard.add_line()
    # keyboard.add_button("Яой", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Юри", color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button("Гарем", color=VkKeyboardColor.POSITIVE)

    # keyboard.add_line()
    # keyboard.add_button("Этти", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()