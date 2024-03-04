from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from advert.services.services import sale_parts_car
from user.services import detect_user
from django.conf import settings

bot = settings.BOT
dp = settings.DP


class PartsCar(StatesGroup):
    mark = State()
    model = State()
    year = State()
    description = State()


async def add_car(message: types.message):
    await PartsCar.mark.set()
    await message.reply('Введите марку автомобиля')


async def add_mark(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data['mark'] = message.text
        await PartsCar.next()
    await message.reply('Теперь введите модель авто')


async def add_model(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data['model'] = message.text
    await PartsCar.next()
    await message.reply("Теперь добавьте год выпуска авто")


async def add_year(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year'] = message.text
    await PartsCar.next()
    await message.reply('Теперь введите описание')


async def add_description(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    pk = await detect_user(message.from_user.username)
    async with state.proxy() as data:
        await sale_parts_car(mark=data['mark'], model=data['model'], year=data['year'], description=data['description'],
                             pk=pk)
        await message.reply(
            f"""
        Вы добавили авто в разборе:
        Марка - {data['mark']},
        Модель - {data['model']},
        Год выпуска - {data['year']}
        Описание - {data['description']}
        """)
    await state.finish()


def register_handlers_sale_parts_car(dp: Dispatcher):
    dp.register_message_handler(add_car, text=['Разместить авто в разборе'], state=None)
    dp.register_message_handler(add_mark, state=PartsCar.mark)
    dp.register_message_handler(add_model, state=PartsCar.model)
    dp.register_message_handler(add_year, state=PartsCar.year)
    dp.register_message_handler(add_description, state=PartsCar.description)
