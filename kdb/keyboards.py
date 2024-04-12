from aiogram import types


def start_keyboard():
    buttons = [
        types.InlineKeyboardButton(
            text='1. Наши товары', callback_data='product'),
        types.InlineKeyboardButton(
            text='2. РОЗЫГРЫШ', callback_data='gift'),
        types.InlineKeyboardButton(
            text='3. Задать вопрос', callback_data='question'),
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[buttons])
    return keyboard


def product_keyboard():
    buttons = [
        types.InlineKeyboardButton(
            text='60*120', callback_data='60*120'),
        types.InlineKeyboardButton(
            text='75*150', callback_data='75*150'),
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[buttons])
    return keyboard


def gift_keyboard():
    buttons = [
        types.InlineKeyboardButton(
            text='1', callback_data='button_gift_1'),
        types.InlineKeyboardButton(
            text='2', callback_data='button_gift_2'),
        types.InlineKeyboardButton(
            text='3', callback_data='button_gift_3'),
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[buttons])
    return keyboard


def gift_ready_or_not():
    buttons = [
        types.InlineKeyboardButton(
            text='Отправить скриншоты', callback_data='button_gift_1'),
        types.InlineKeyboardButton(
            text='Задать вопрос', callback_data='button_gift_3'),
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[buttons])
    return keyboard


def gift_yes_or_no():
    buttons = [
        types.InlineKeyboardButton(
            text='Да участвует', callback_data='verification_yes'),
        types.InlineKeyboardButton(
            text='Нет не участвует', callback_data='verification_no'),
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[buttons])
    return keyboard


def get_admin_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(
                text='Розыгрыш', callback_data='prize'
            )
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
