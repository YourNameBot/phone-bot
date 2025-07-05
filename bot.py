from aiogram import Bot, Dispatcher, types
from aiogram import F  # أضف هذا السطر الجديد

bot = Bot(token="TOKEN")  # احتفظ بالتوكن كما هو
dp = Dispatcher()

@dp.message(F.text == '/start')  # نفس السطر الذي استخدمته لكن الآن سيعمل
async def start(message: types.Message):
    await message.answer("أهلاً بك! البوت يعمل الآن 🎉")

dp.run_polling(bot)
