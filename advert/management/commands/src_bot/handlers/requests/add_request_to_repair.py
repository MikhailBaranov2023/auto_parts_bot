from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from advert.services.services import create_requests_to_repair
from user.services import detect_user
from django.conf import settings

bot = settings.BOT
dp = settings.DP


class Request(StatesGroup):
    country = State()
    city = State()
    description = State()


# @dp.message_handlers(text=['Запрос на ремонт'], state=None)
async def add_request(message: types.Message, ):
    await Request.country.set()
    await message.reply('Введите страну')


# @dp.message_handlers(state=Request.country)
async def add_country(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['country'] = message.text
        await Request.next()
    await message.reply('Введите город')


# @dp.message_handlers(state=Request.city)
async def add_city(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        await Request.next()
    await message.reply('Введите подробное описание нобоходимого ремонта')


# @dp.message_handlers(state=Request.description)
async def add_description(message: types.Message, state=FSMContext):
    pk = await detect_user(message.from_user.username)
    async with state.proxy() as data:
        data['description'] = message.text
    async with state.proxy() as data:
        await create_requests_to_repair(country=data['country'], city=data['city'], description=data['description'],
                                        pk=pk)
        await message.reply(f"""
                Вы создали запрос на ремонт авто:
                Срана - {data['country']},
                Город - {data['city']},
                Описание поломки - {data['description']}
                """)
    await state.finish()


def register_handlers_add_request_to_repair(dp: Dispatcher):
    dp.register_message_handler(add_request, text=['Запрос на ремонт'], state=None)
    dp.register_message_handler(add_country, state=Request.country)
    dp.register_message_handler(add_city, state=Request.city)
    dp.register_message_handler(add_description, state=Request.description)
