import logging
from googletrans import Translator

from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram import Router, types, Bot
from aiogram.types import Message

from core.models.text_to_image import TextToImage
from core.utils.data import config
from core.utils.db_postgres_api import quick_commands
from core.utils.db_postgres_api.db_telegram import db
from core.utils.user_inputs import GetUserInput


router = Router()


# TODO: 1. Получаем каманду
# TODO: 2. Пока не получаем запрос "закончить" от пользователя
# TODO: 3. Получаем запрос от пользователя на генерацию
# TODO: 4. Генерация изображения
# TODO: 5. Обновления статуса по команде
@router.message(Command("image_generation"))
async def get_input_image_generation(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Когда захотите закончить генерацию, введите - /cancel. Напишите, "
                         "что вы хотели бы видеть на картине?")
    res = await state.set_state(GetUserInput.user_input)


@router.message(StateFilter(GetUserInput.user_input), ~Command('cancel'))
async def text_to_image_result(message: Message, bot: Bot, state: FSMContext):

    await state.update_data(user_input=message.text)
    user_inputs = await state.get_data()
    text = user_inputs.get('user_input')

    # Добавляем записи в таблицу
    await db.set_bind(config.POSTGRES_URI)
    await quick_commands.add_user(str(message.from_user.id), message.from_user.full_name, text)

    if text:
        await bot.send_message(message.chat.id, text="Окей! Дай немного времени, пока я делаю работу за тебя 😜")
        translator = Translator()
        res = translator.translate(text, src='ru')

        model = TextToImage(config.HUG_FACE_API_TOKEN,
                            config.HUG_FACE_URL)  # By API
        # TODO: Обработать ошибку и перезапуск команды через некоторое время:
        #  aiogram.exceptions.TelegramBadRequest: Telegram server says - Bad Request: IMAGE_PROCESS_FAILED
        img_bytes = model.prompt(res.text)
        # image = Image.open(io.BytesIO(img_bytes))
        #
        # bio = io.BytesIO()
        # bio.name = 'image.jpeg'
        # image.save(bio, 'JPEG')
        # bio.seek(0)

        # await message.reply_document(document=types.BufferedInputFile(
        #     file=bio.getvalue(),
        #     filename='your_image.jpeg'
        #     )
        # )
        # РАБОТАЕТ!!!!!
        # await message.reply_document(document=types.BufferedInputFile(
        #     file=img_bytes,
        #     filename='your_image.jpeg'
        # ))

        # РАБОТАЕТ!!!!!
        await bot.send_photo(message.chat.id, photo=types.BufferedInputFile(
            file=img_bytes,
            filename='your_image.jpeg'
        ))


@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command_state(message: Message):
    await message.answer(
        text='ОК. Вы вышли из машины состояний\n\n'
             'Удалять нечего'
    )


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text='Вы вышли из машины состояний\n\n'
             'Чтобы снова выбрать необходимую функцию введите - /help'
    )
    bind = db.pop_bind()
    if bind:
        logging.info("Подключение к PostgreSQL закрыто")
        await bind.close()
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()
