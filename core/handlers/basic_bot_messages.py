import io
from PIL import Image
from googletrans import Translator

from aiogram import Router, Bot, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from core.models.text_to_image import TextToImage
# from core.settings import config
from core.utils.data import config

router = Router()


@router.startup()
async def start_bot(bot: Bot):
    await bot.send_message(config.ADMIN_ID, 'Бот запущен')


@router.shutdown()
async def start_bot(bot: Bot):
    await bot.send_message(config.ADMIN_ID, 'Бот остановлен')


@router.message(CommandStart())
async def handle_start(message: Message):
    await message.answer(text=f"Приветствую, {message.from_user.first_name}! Я бот, который обладает интересным функционалом.\n"
                              f"Нажми или введи - /help и ты увидешь, что я умею.")


@router.message(Command("help", ignore_case=True))
async def handle_help(message: Message):
    await message.answer(text=f"Что имеем:\n"
                              
                              f"/image_generation - Создам изображение по вашему текстовому сообщению. Презентация, "
                              f"аватарка, заставка, поздравление и тд\n"
                              
                              f"/image_aug - Изменю ваше изображение с желаемыми характеристаками\n"
                              
                              f"/gpt4 - ChatGPT4. Есть ограничение на количество выдаваемых токенов. Код для решения "
                              f"задачи, реферат, справка по интересующей теме, генерация текста и тд\n\n"
                              
                              f"/help - справка по разделам")


@router.message()
async def empty_message(message: Message):
    await message.answer(
        text=f"Для начала работы со мной, выбери пожалуйста, что тебя интересует из "
             f"списка моих возможностей введя команду - /help")
