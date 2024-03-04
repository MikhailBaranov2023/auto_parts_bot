from aiogram import types
from advert.management.commands.src_bot.keyboards.keyboards import main_menu, advert_menu, request_menu, profile_menu, \
    sale_auto_menu, cars_to_parts_menu
from aiogram import Dispatcher
from django.conf import settings

bot = settings.BOT
dp = settings.DP


async def command_start(message: types.Message):
    # await bot.send_message(message.from_user.id, message.chat.id)
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, Добро пожаловать в наш бот',
                           reply_markup=main_menu)


async def bot_menu(message: types.Message):
    if message.text == "Объявления":
        await bot.send_message(message.from_user.id, message.text, reply_markup=advert_menu)
    elif message.text == 'Создать запрос':
        await bot.send_message(message.from_user.id, message.text, reply_markup=request_menu)
    elif message.text == 'Профиль':
        await bot.send_message(message.from_user.id, message.text, reply_markup=profile_menu)
    elif message.text == 'Продать авто':
        await bot.send_message(message.from_user.id, message.text, reply_markup=sale_auto_menu)
    elif message.text == 'Авто в разборе':
        await bot.send_message(message.from_user.id, message.text, reply_markup=cars_to_parts_menu)
    # else:
    #     await bot.send_message(message.from_user.id, 'пожалуйста выберите интересующий пункт из меню',
    #                            reply_markup=main_menu)


def register_handlers_for_menu(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(bot_menu)
