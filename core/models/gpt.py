# from aiogram import types, Bot
# import g4f
# from aiogram.fsm.context import FSMContext
#
# from core.utils.data import config
# from core.utils.db_postgres_api import quick_commands
# from core.utils.db_postgres_api.db_telegram import db
# from core.utils.user_inputs import GetUserInput
# from aiogram import Router
# from aiogram.filters import Command, StateFilter
#
# router = Router()
#
# # Словарь для хранения истории разговоров
# conversation_history = {}
#
#
# # Обработчик для каждого нового сообщения
# @router.message(Command("gpt4"))
# async def send_welcome(message: types.Message, state: FSMContext):
#     await message.answer("Когда захотите закончить разговор со мной, введите - /cancel. Напишите, "
#                          "что вы хотели бы обсудить?")
#     res = await state.set_state(GetUserInput.user_input)
#
#
# @router.message(StateFilter(GetUserInput.user_input), ~Command('cancel'))
# async def send_welcome(message: types.Message, bot: Bot, state: FSMContext):
#
#     await state.update_data(user_input=message.text)
#     user_inputs = await state.get_data()
#     text = user_inputs.get('user_input')
#
#     # Добавляем записи в таблицу
#     # await db.set_bind(config.POSTGRES_URI)
#     # await quick_commands.add_user(str(message.from_user.id), message.from_user.full_name, text)
#
#     user_id = message.from_user.id
#     user_input = text
#
#     if user_id not in conversation_history:
#         conversation_history[user_id] = []
#
#     conversation_history[user_id].append({"role": "user", "content": user_input})
#     conversation_history[user_id] = trim_history(conversation_history[user_id])
#
#     chat_history = conversation_history[user_id]
#
#     try:
#         response = await g4f.ChatCompletion.create_async(
#             model=g4f.models.default,
#             messages=chat_history,
#             provider=g4f.Provider.Bing,
#         )
#         chat_gpt_response = response
#     except Exception as e:
#         print(f"{g4f.Provider.GeekGpt.__name__}:", e)
#         chat_gpt_response = "Извините, произошла ошибка."
#
#     conversation_history[user_id].append({"role": "assistant", "content": chat_gpt_response})
#     print(conversation_history)
#     length = sum(len(message["content"]) for message in conversation_history[user_id])
#     print(length)
#     await message.answer(chat_gpt_response)
#
#
# # Функция для обрезки истории разговора
# def trim_history(history, max_length=4096):
#     current_length = sum(len(message["content"]) for message in history)
#     while history and current_length > max_length:
#         removed_message = history.pop(0)
#         current_length -= len(removed_message["content"])
#     return history
#
#
# @router.message(Command("clear"))
# async def process_clear_command(message: types.Message):
#     user_id = message.from_user.id
#     conversation_history[user_id] = []
#     await message.reply("История диалога очищена.")
