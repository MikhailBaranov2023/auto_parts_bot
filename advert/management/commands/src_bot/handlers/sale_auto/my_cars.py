from aiogram import Dispatcher
from aiogram import types
from advert.services.services import detect_my_cars_to_sale, detect_my_cars_to_parts
from user.services import detect_user
from django.conf import settings

bot = settings.BOT
dp = settings.DP


# @dp.message_handlers(text=['Мои авто на продаже'])
async def get_my_car_to_sale(message: types.Message):
    pk = await detect_user(message.from_user.username)
    await message.reply(await detect_my_cars_to_sale(pk=pk))


# @dp.message_handlers(text=['Мои авто в разборе'])
async def get_my_car_to_parts(message: types.Message):
    pk = await detect_user(message.from_user.username)
    await message.reply(await detect_my_cars_to_parts(pk=pk))


def register_handlers_my_cars(dp: Dispatcher):
    dp.register_message_handler(get_my_car_to_sale, text=['Мои авто на продаже'])
    dp.register_message_handler(get_my_car_to_parts, text=['Мои авто в разборе'])
