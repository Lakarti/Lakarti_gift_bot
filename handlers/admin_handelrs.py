import aiomysql

from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State

from kdb.keyboards import get_admin_keyboard
from DB.db import async_connect_to_db, check_is_winner
from utils.config import read_config


config = read_config('settings.ini')

admin_router = Router()


class SendMessage(StatesGroup):
    Message_from_admin = State()
    User_id = State()


ADMIN_USER_IDS = [config['Admin_users']['1'],
                  config['Admin_users']['2']]


@admin_router.message(Command('admin'))
async def admin_panel(message: types.Message):
    chat_id = message.from_user.id

    # Получение подключения к базе данных
    connection = await async_connect_to_db()
    async with connection.cursor() as cur:
        cur: aiomysql.Cursor
        # Получение информации о пользователе из базы данных
        await cur.execute("SELECT is_admin FROM users WHERE chat_id = %s", (chat_id,))
        result = await cur.fetchone()

        if result and result[0] == 1:  # Если пользователь - администратор
            keyboard = get_admin_keyboard()

            # Отправка сообщения с клавиатурой
            await message.reply('Выберите действие:', reply_markup=keyboard)


@admin_router.callback_query(F.data == 'prize')
async def prepare_for_send(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите id пользователя, которому хотите отправить сообщение о выйгрыше')
    await state.set_state(SendMessage.Message_from_admin)


@admin_router.message(SendMessage.Message_from_admin)
async def send_for_winner(message: types.Message, state: FSMContext, bot: Bot):
    winner_id = message.text
    is_winner = await check_is_winner(winner_id)

    if not is_winner:
        await message.reply('Данный пользователь не является участником конкурса')
        return

    await bot.send_message(winner_id, text='Добрый день! Поздравляем Вас с Победой в нашем розыгрыше!\n\
Cвяжитесь с нами и выберем коврик и адрес отправки.\n\
https://t.me/Lakarti_sales')

    await state.clear()
