import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = ""

url_git = "https://github.com/GL1KK"

url_tg = "https://t.me/programisticDanya"

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"Привет я Даня мой гитхаб: {url_git}")
@dp.message(Command("info"))
async def info_handler(message: Message):
    await message.answer(f"Мне лень тут писать чек тгк: {url_tg}")
@dp.message(Command("write"))
async def write_handler(message: Message):
    await message.answer("Напиши что то и я мб отвечу)")
    @dp.message(lambda message: message.text)
    async def to_me_handler(message: Message):
        await message.send_copy(chat_id=1965822435)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())