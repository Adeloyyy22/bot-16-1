from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, ADMIN, dp





# @dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Салам хозяин {message.from_user.full_name}")

async def show_random_user(message: types.Message):
    await bot.db.sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=["start"])
    dp.register_message_handler(show_random_user, commands=["random"])