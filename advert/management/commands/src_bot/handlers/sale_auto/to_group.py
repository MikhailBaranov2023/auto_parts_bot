from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from django.conf import settings

bot = settings.BOT
dp = settings.DP


# @dp.message_handler(commands=['start'])
async def go_to_group(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="перейти в группу", url="https://t.me/+pnYgJMix-7NhNmQy")
    keyboard.add(button)
    await bot.send_message(message.from_user.id, "Для просмотра объявлений перейдите в группу", reply_markup=keyboard)


def register_handler_to_group(dp: Dispatcher):
    dp.register_message_handler(go_to_group, text=['Поиск по авто'])
