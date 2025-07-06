from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import os

bot = Bot(token=os.getenv('TOKEN'))  # TOKEN بأحرف كبيرة
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🎉 البوت يعمل الآن بنجاح!")

@dp.message(F.text == '/test')
async def test(message: types.Message):
    await message.answer("✅ كل شيء يعمل بشكل صحيح")

if __name__ == '__main__':
    dp.run_polling(bot)
