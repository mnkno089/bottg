import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
from rash import kb1
from randfox import fox

#Включаем логирование
logging.basicConfig(level=logging.INFO)

#Создаем объект бота
bot = Bot(token=config.token)

#Диспетчер
dp = Dispatcher()


#Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Привет, {name}", reply_markup=kb1)

#Хэндлер на команду /stop
@dp.message(Command("stop"))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Пока, {name}")


#Хэндлер на команду /fox
@dp.message(Command("fox"))
@dp.message(Command("лиса"))
@dp.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f"Держи лису, {name}")
    await message.answer_photo(photo=img_fox)



#Хендлер на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text
    name = message.chat.first_name
    if "Привет" in msg_user:
        await message.answer(f"Привет, {name}")
    elif "Пока" in msg_user:
        await message.answer(f"Пока-пока  {name}")
    elif "лиса" in msg_user:
        await message.answer(f"Смотри что у меня есть, {name}", reply_markup=kb1)
    else:
        await message.answer(f"Я не знаю таких слов")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())