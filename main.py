import asyncio
import logging

from aiogram import Bot, Router
from aiogram import Dispatcher

from core.filters import filter_media
from core.models import text_to_image, gpt
from core.handlers import basic_bot_messages, models_messages
from core.utils.data import config

router = Router()


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(
        models_messages.router,
        # gpt.router,
        basic_bot_messages.router,
        filter_media.router,
        text_to_image.router
    )

    # Сбор логов работы и вывод в консоли
    logging.basicConfig(level=logging.INFO)
    # Старт опроса
    try:
        # Чтобы при запуске бота не учитывались команды от пользователей, которые были отправлены в выключенной
        # стадии бота
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, handle_as_tasks=False)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
