# from aiogram import Bot, types, Router
# from aiogram.types import Message
# from googletrans import Translator
#
# from core.models.text_to_image import TextToImage
# from core.settings import config
#
# router = Router()
#
# # Нужно придумать, как обработать ошибку, когда проблема на стороне сервера - b"{error: Internal server error}"
# async def model_start(message: Message, bot: Bot):
#     translator = Translator()
#     res = translator.translate(message.text, src='ru')
#
#     model = TextToImage(config.hug_face_api_token.get_secret_value(),
#                         config.hug_face_url.get_secret_value())  # By API
#
#     #
#     img_bytes = model.prompt(res.text)
#     if img_bytes == b"{error: Internal server error}":
#         print(img_bytes)
#         print(type(img_bytes))
#         return False
#     else:
#         await bot.send_photo(message.chat.id, photo=types.BufferedInputFile(
#             file=img_bytes,
#             filename='your_image.jpeg'
#         ))
#         return True
#
#
# @router.message()
# async def text_to_image_result(message: Message, bot: Bot):
#     """
#     Deploy by HuggingFace API
#     :param message: Telegram Message from user
#     :param bot: Bot instance from aiogram
#     :return: Image to user
#     """
#     await message.answer(text="Человеку будет дан ответ, но ему придется подождать пару минут пока я рисую!")
#
#     if message.text:
#         while not model_start(message=message, bot=bot):
#             await model_start(message=message, bot=bot)
