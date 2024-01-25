from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Смайлы"),
            KeyboardButton(text="Ссылки")
        ],
        [
            KeyboardButton(text="Калькулятор"),
            KeyboardButton(text="Спец. кнопки")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)


spec = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить ГЕО", request_location=True),
            KeyboardButton(text="Отправить контакт", request_contact=True),
            KeyboardButton(text="Отправить опрос", request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text="НАЗАД")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)