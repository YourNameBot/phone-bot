from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🎉 البوت يعمل بنجاح!")

@dp.message(F.text == '/help')
async def help(message: types.Message):
    await message.answer("أرسل /start للتأكد من العمل")

if __name__ == '__main__':
    dp.run_polling(bot)
