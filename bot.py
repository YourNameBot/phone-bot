from aiogram import Bot, Dispatcher, types
from aiogram import F  # هذا السطر الجديد مهم جداً
from aiogram.filters import Command  # أضف هذا أيضاً

bot = Bot(token="TOKEN")  # سيتم استبدال TOKEN تلقائياً من متغيرات البيئة
dp = Dispatcher()

# الطريقة الأولى (مباشرة باستخدام F)
@dp.message(F.text == '/start')
async def start(message: types.Message):
    await message.answer("مرحباً! البوت يعمل الآن بنجاح 🎉")

# الطريقة الثانية (باستخدام Command)
@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer("أنا بوت مساعد، جرب /start")

dp.run_polling(bot)
