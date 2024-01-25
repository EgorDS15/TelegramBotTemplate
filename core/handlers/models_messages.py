import io
from PIL import Image
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from googletrans import Translator

from aiogram import Router, types, Bot
from aiogram.types import Message

from core.models.text_to_image import TextToImage
from core.settings import config
from core.utils.user_inputs import GetUserInput


router = Router()


# TODO: 1. Получаем каманду
# TODO: 2. Пока не получаем запрос "закончить" от пользователя
# TODO: 3. Получаем запрос от пользователя на генерацию
# TODO: 4. Генерация изображения
# TODO: 5. Обновления статуса по команде
@router.message(Command("image_generation"))
async def get_input_image_generation(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Когда захотите закончить генерацию, введите - /cancel. Напишите, что вы хотели бы видеть на картине?")
    res = await state.set_state(GetUserInput.user_input)


@router.message(StateFilter(GetUserInput.user_input), ~Command('cancel'))
async def text_to_image_result(message: Message, bot: Bot, state: FSMContext):
    # res = await state.set_state(GetUserInput.user_input)
    await state.update_data(user_input=message.text)
    user_inputs = await state.get_data()
    text = user_inputs.get('user_input')

    if text:
        await bot.send_message(message.chat.id, text="Окей! Дай немного времени, пока я делаю работу за тебя 😜")
        translator = Translator()
        res = translator.translate(text, src='ru')

        model = TextToImage(config.hug_face_api_token.get_secret_value(),
                            config.hug_face_url.get_secret_value())  # By API

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
             'Чтобы снова перейти к заполнению анкеты - '
             'отправьте команду'
    )
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()
