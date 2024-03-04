from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from advert.services.services import create_request_to_unit
from user.services import detect_user
from django.conf import settings

bot = settings.BOT
dp = settings.DP

class Request(StatesGroup):
    mark_auto = State()
    model_auto = State()
    year_auto = State()
    description = State()


# @dp.message_handlers(text=['Запрос на запчасть'], state=None)
async def add_request(message: types.Message):
    await Request.mark_auto.set()
    await message.reply('Введите марку автомобиля')


# @dp.message_handlers(state=Request.mark_auto)
async def add_mark_auto(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['mark_auto'] = message.text
        await Request.next()
    await message.reply('Введите модель авто')


# @dp.message_handlers(state=Request.model_auto)
async def add_model_auto(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['model_auto'] = message.text
        await Request.next()
    await message.reply('Введите год выпуска авто')


# @dp.message_handlers(state=Request.year_auto)
async def add_year(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['year_auto'] = message.text
        await Request.next()
    await message.reply('А теперь введите описание')


# @dp.message_handlers(state=Request.description)
async def add_description(message: types.Message, state=FSMContext):
    pk = await detect_user(message.from_user.username)

    async with state.proxy() as data:
        data['description'] = message.text

    async with state.proxy() as data:
        await create_request_to_unit(mark_auto=data['mark_auto'], model_auto=data['model_auto'],
                                     year_auto=data['year_auto'],
                                     description=data['description'], pk=pk)
        await message.reply(f"""
        Вы создали запрос на агрегат для машины:
        марка - {data['mark_auto']},
        модель - {data['model_auto']},
        год выпуска - {data['year_auto']},
        описание - {data['description']}
        """)
    await state.finish()


def register_handlers_add_request_to_unit(dp: Dispatcher):
    dp.register_message_handler(add_request, text=['Запрос на агрегат'], state=None)
    dp.register_message_handler(add_mark_auto, state=Request.mark_auto)
    dp.register_message_handler(add_model_auto, state=Request.model_auto)
    dp.register_message_handler(add_year, state=Request.year_auto)
    dp.register_message_handler(add_description, state=Request.description)
