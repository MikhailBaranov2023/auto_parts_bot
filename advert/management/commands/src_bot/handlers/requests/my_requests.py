from aiogram import Dispatcher
from aiogram import types
from advert.services.services import detect_my_requests_to_parts, detect_my_requests_to_unit, \
    detect_my_requests_to_repair
from user.services import detect_user
from django.conf import settings

bot = settings.BOT
dp = settings.DP


# @dp.message_handlers(text=['Мои запросы'])
async def get_my_request(message: types.Message):
    pk = await detect_user(message.from_user.username)
    await message.reply(await detect_my_requests_to_parts(pk=pk))
    await message.reply(await detect_my_requests_to_unit(pk=pk))
    await message.reply(await detect_my_requests_to_repair(pk=pk))


def register_handlers_my_requests(dp: Dispatcher):
    dp.register_message_handler(get_my_request, text=['Мои запросы'])
