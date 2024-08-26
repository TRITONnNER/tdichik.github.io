from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor

bot = Bot(token='YOUR_BOT_TOKEN')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="Play Hamster Clicker",
            web_app=WebAppInfo(url="https://your-webapp-url.com")
        )
    )
    await message.answer("Click the button to play the game!", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)
