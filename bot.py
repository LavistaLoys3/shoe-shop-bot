from aiogram import Bot, Dispatcher, types
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Вітаю в магазині взуття 👟! Скоро все буде працювати.")

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
