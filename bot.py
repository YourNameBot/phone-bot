from aiogram import Bot, Dispatcher, types
import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

@dp.message(commands=['start'])
async def start(message: types.Message):
    await message.answer("🎉 مرحبًا! أنا بوت الأرقام الجاهز!")

if __name__ == "__main__":
    dp.run_polling(bot)
