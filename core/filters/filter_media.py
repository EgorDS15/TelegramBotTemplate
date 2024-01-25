from aiogram import F
from aiogram.types import Message
from aiogram import Router

router = Router()


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"Пока что я не работаю с изображениями, но скоро начну;)")
