from aiogram import types


button1 = types.KeyboardButton(text="/start")
button2 = types.KeyboardButton(text="Стоп")
button3 = types.KeyboardButton(text="Инфо")
button4 = types.KeyboardButton(text="Покажи лису")
button5 = types.KeyboardButton(text="Закрыть")

keyword1 = [
    [button1, button2,button5],
    [button3,button4]
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyword1, resize_keyboard=True)