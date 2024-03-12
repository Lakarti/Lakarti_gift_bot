import keyboards
import asyncio
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InputMediaPhoto
from aiogram import exceptions
from aiogram import Bot
from db import insert_user_data, update_participation_number, get_participation_value
from logger_config import logging


router = Router()
handlers_logger = logging.getLogger('code_logger')

class ScreenshotsState(StatesGroup):
    review_screenshot = State()
    purchase_screenshot = State()
    verification = State()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    keyboard = keyboards.start_keyboard()
    chat_id = message.chat.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    await insert_user_data(chat_id, username, first_name, last_name)

    await message.answer('Привет!\n\
На связи команда RichCat. \n\
Спасибо, что выбрали нас! \n\n\
Здесь вы можете ознакомиться с нашим ассортиментом, а также принять участие в РОЗЫГРЫШЕ ЗА ОТЗЫВ\n\n\
Для этого выберите соответствующий пункт\n', reply_markup=keyboard)


@router.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer('Вы можете задать свой вопрос в нашем чате. https://t.me/RichCat_help_bot')


@router.callback_query(F.data == 'product')
async def products(calllback: types.CallbackQuery):
    keyboard = keyboards.product_keyboard()
    await calllback.message.answer('Выбор размера', reply_markup=keyboard)


@router.callback_query(F.data == '60*120')
async def products_60_120(callback: types.CallbackQuery):
    photo_urls = [
        'https://basket-09.wbbasket.ru/vol1267/part126758/126758787/images/big/1.webp',
        'https://basket-13.wbbasket.ru/vol1940/part194079/194079890/images/big/1.webp',
        'https://basket-13.wbbasket.ru/vol1940/part194079/194079888/images/big/1.webp',
        'https://basket-13.wbbasket.ru/vol1940/part194079/194079894/images/big/1.webp',
        'https://basket-09.wbbasket.ru/vol1260/part126025/126025374/images/big/1.webp',
        'https://basket-09.wbbasket.ru/vol1267/part126756/126756271/images/big/1.webp',
    ]
    product_url = ['https://www.wildberries.ru/catalog/126758787/detail.aspx',
                   'https://www.wildberries.ru/catalog/194079890/detail.aspx',
                   'https://www.wildberries.ru/catalog/194079888/detail.aspx',
                   'https://www.wildberries.ru/catalog/194079894/detail.aspx',
                   'https://www.wildberries.ru/catalog/126025374/detail.aspx',
                   'https://www.wildberries.ru/catalog/126756271/detail.aspx'
                   ]

    message_text = (
        f'1: <a href="{product_url[0]}">126758787</a>\n'
        f'2: <a href="{product_url[1]}">194079890</a>\n'
        f'3: <a href="{product_url[2]}">194079888</a>\n'
        f'4: <a href="{product_url[3]}">194079894</a>\n'
        f'5: <a href="{product_url[4]}">126025374</a>\n'
        f'6: <a href="{product_url[5]}">126756271</a>'

    )

    media_group = []
    for photo_url in photo_urls:
        media_group.append(InputMediaPhoto(media=photo_url, caption="text"))

    # Отправка фотографий в группе в одном сообщении
    await callback.message.answer_media_group(media=media_group)

    # Отправка ссылки на товар
    await callback.message.answer(message_text, parse_mode='HTML')


@router.callback_query(F.data == '75*150')
async def products_60_120(callback: types.CallbackQuery):
    photo_urls = [
        'https://basket-13.wbbasket.ru/vol1940/part194079/194079892/images/big/1.webp',
        'https://basket-13.wbbasket.ru/vol1940/part194079/194079893/images/big/1.webp',
        'https://basket-13.wbbasket.ru/vol1940/part194079/194079891/images/big/1.webp',
        'https://basket-09.wbbasket.ru/vol1286/part128615/128615052/images/big/1.webp',
        'https://basket-09.wbbasket.ru/vol1286/part128603/128603867/images/big/1.webp'
    ]
    product_url = ['https://www.wildberries.ru/catalog/194079892/detail.aspx',
                   'https://www.wildberries.ru/catalog/194079893/detail.aspx',
                   'https://www.wildberries.ru/catalog/194079891/detail.aspx',
                   'https://www.wildberries.ru/catalog/128615052/detail.aspx',
                   'https://www.wildberries.ru/catalog/128603867/detail.aspx']

    message_text = (
        f'1: <a href="{product_url[0]}">194079892</a>\n'
        f'2: <a href="{product_url[1]}">194079893</a>\n'
        f'3: <a href="{product_url[2]}">194079891</a>\n'
        f'4: <a href="{product_url[3]}">128615052</a>\n'
        f'5: <a href="{product_url[4]}">128603867</a>'
    )

    media_group = []
    for photo_url in photo_urls:
        media_group.append(InputMediaPhoto(media=photo_url, caption="text"))

    # Отправка фотографий в группе в одном сообщении
    await callback.message.answer_media_group(media=media_group)

    # Отправка ссылки на товар
    await callback.message.answer(message_text, parse_mode='HTML')


@router.callback_query(F.data == 'gift')
async def gift_handler(callback: types.CallbackQuery):
    text = '''Благодарим за выбор нашего бренда. Это нас очень вдохновляет продолжать Вас радовать.
Для нас важно Ваше мнение о наших коврах.
Поэтому мы решили КАЖДЫЙ МЕСЯЦ проводить РОЗЫГРЫШ среди любимых покупателей за отзыв и дарить один из наших прекрасных КОВРИКОВ из эко-меха 60*120 см (цвет выберет победитель из тех, что в наличии)

УСЛОВИЯ УЧАСТИЯ:
Вам нужно оставить отзыв в феврале 2024, марте 2024:
Напишите, что вам понравилось в коврах RichCat
Прикрепите фото (это по желанию, но нам будет приятно).
За каждый новый отзыв Вам присваивается порядковый номер для розыгрыша, который будет Вам прислан после выполнения условий

❗️Обратите внимание на то, чтобы наш секретный вкладыш не попал в кадр. О нем знаем только мы с Вами😉

🚩Итоги подведём 8 апреля в нашем Telegram-канале https://t.me/richcatkovry

Для того, чтобы принять участие, выбирайте соответствующий пункт
'''
    await callback.message.answer(text)

    await asyncio.sleep(2)
    await callback.message.answer('''🚩 Нажмите 1: если вы уже оставили отзыв
🚩 Нажмите 2: если вы еще не оставили отзыв
🚩 Нажмите 3: если возник вопрос/проблема''', reply_markup=keyboards.gift_keyboard())


@router.callback_query(F.data == 'button_gift_1')
async def gift_button_1(callback: types.CallbackQuery, state: FSMContext):
    text = '''Для того, чтобы вам присваивался порядковый Номер в Розыгрыше необходимо отправить в этот чат два скриншота из вашего кабинета.
Сначала отправьте скриншот готового отзыва, как на примере.

'''
    # Получение текущего значения participate
    chat_id = callback.message.chat.id
    participate_value = await get_participation_value(chat_id)

    if participate_value == 1:
        # Добавить куда написать.
        text = "Вы уже участвуете в конкурсе! Если у вас появились вопросы напишите нам https://t.me/RichCat_help_bot ."
        await callback.message.answer(text)
    else:
        await callback.message.answer(text)
        await callback.message.answer_photo('https://lakarti.ru/image/catalog/photo_for_bot/IMG_8256.JPG')

        # Переходим к ожиданию первого скриншота (отзыва)
        await state.set_state(ScreenshotsState.review_screenshot)


@router.message(ScreenshotsState.review_screenshot)
async def process_review_screenshot(message: types.Message, state: FSMContext):
    if not message.photo:
        # Пользователь не отправил фотографию
        await message.answer('Пожалуйста, отправьте фото вашего отзыва.')
        return

    # Сохраняем первый скриншот (отзыв)
    review_screenshot = message.photo[-1].file_id
    await state.update_data(review_screenshot=review_screenshot)

    # Переходим к ожиданию второго скриншота (покупки)
    await state.set_state(ScreenshotsState.purchase_screenshot)
    await message.answer('''Отлично! Теперь отправьте скриншот нашего товара из раздела "Покупки", как на примере.''')
    await message.answer_photo('https://lakarti.ru/image/catalog/photo_for_bot/IMG_8255.JPG')


@router.message(ScreenshotsState.purchase_screenshot)
async def process_verification_screenshot(message: types.Message, state: FSMContext, bot: Bot):
    if not message.photo:
        # Пользователь не отправил фотографию
        await message.answer('Пожалуйста, отправьте фото вашей покупки.')
        return
    # Сохраняем второй скриншот (покупку)
    purchase_screenshot = message.photo[-1].file_id
    chat_id = message.chat.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    await state.update_data(purchase_screenshot=purchase_screenshot)
    await state.update_data(chat_id=chat_id)

    # В данном месте у вас уже будут оба скриншота в данных состояния
    # Вы можете выполнить дополнительные действия или перейти к следующему этапу
    data = await state.get_data()
    review_screenshot = data.get('review_screenshot')
    purchase_screenshot = data.get('purchase_screenshot')

    # Отправляем скриншоты в личный чат для проверки
    user_id_to_check = 1746665613  # Замените на фактический идентификатор пользователя
    await bot.send_photo(user_id_to_check, review_screenshot)
    await bot.send_photo(user_id_to_check, purchase_screenshot, reply_markup=keyboards.gift_yes_or_no(), caption=f'{chat_id, username, first_name, last_name}')
    # Можно добавить ещё имя фамилю пользователя что отправляет сообщение.

    # Отправляем пользователю сообщение об успешной отправке
    await message.answer('Скриншоты успешно отправлены на проверку. Ожидайте результатов.')

    # await state.set_state


@router.callback_query(F.data == "verification_yes")
async def process_verification_response(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    caption = callback.message.caption
    chat_id = caption.split(',')[0].strip('()')
    number = await update_participation_number(chat_id)
    text = f'''Поздравляем, Вы среди участников нашего розыгрыша, который состоится \
    5 февраля в 15.00 в прямом эфире в нашем телеграм-канале https://t.me/richcatkovry.\
    
Ваш порядковый номер <b>{number}</b>. Удачи!'''
    try:
        await bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML')
        await callback.message.answer("Данные подтверждены")
        await state.clear()
    except exceptions.TelegramBadRequest as e:
        print(e)


@router.callback_query(F.data == "verification_no")
async def process_verification_response(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    chat_id = callback.message.caption
    text = f'''Извините, но похоже, вы отправили не те скриншоты. Пожалуйста, отправьте корректные скриншоты.
Вы можете задать свой вопрос в нашем чате.'''
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboards.gift_ready_or_not(), parse_mode='HTML')
    await callback.message.answer("Данные отклонены.")
    state.set_state(ScreenshotsState.purchase_screenshot)


@router.callback_query(F.data == 'ask_question_gift')
async def ask_question_button(callback: types.CallbackQuery):
    # Перенаправьте пользователя на чат для задания вопроса
    await callback.message.answer("Вы можете задать свой вопрос в нашем чате. https://t.me/RichCat_help_bot ")
    # Здесь вы можете добавить логику перенаправления пользователя или использовать метод, который подходит для вашего случая
    # Например, использовать types.Bot.send_message с текстом, направленным в нужный чат.


@router.callback_query(F.data == 'button_gift_2')
async def gift_button_2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('''Для того, чтобы оставить отзыв, Следуйте по пунктам, и у Вас все получится 🤍:

1️⃣ Зайдите в Личный кабинет
2️⃣ Найдите раздел “Покупки”
3️⃣ Выберите товар Richcat, который Вы приобрели.
4️⃣ Кликните на “Отзыв”, далее – “Оставить отзыв”
5️⃣ Напишите, чем Вам понравился наш бренд
6️⃣ Кликните “Опубликовать отзыв”
7️⃣ Сделайте скриншот готового отзыва
8️⃣ Сделайте скриншот нашего товара из раздела "Покупки"

Сначала отправьте скриншот готового отзыва в этот чат

''')
    await state.set_state(ScreenshotsState.review_screenshot)


@router.callback_query(F.data == 'button_gift_3')
async def gift_button_3(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Вы можете задать свой вопрос в нашем чате. https://t.me/RichCat_help_bot')


@router.message()
async def cmd_default(message: types.Message):
    await message.answer('Для получения информации введите команду /start .')
