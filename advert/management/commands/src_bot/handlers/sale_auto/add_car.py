from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from advert.services.services import sale_car
from user.services import detect_user
from django.conf import settings

bot = settings.BOT
dp = settings.DP


class Car(StatesGroup):
    mark = State()
    model = State()
    year = State()
    image = State()
    description = State()


# @dp.message_handler(text=['Разместить авто для продажи'], state=None)
async def add_car(message: types.Message):
    await Car.mark.set()
    await message.reply('Введите марку автомобиля')


# @dp.message_handler(state=Car.mark)
async def add_mark(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mark'] = message.text
        await Car.next()
    await message.reply('Теперь введите модель авто')


# @dp.message_handler(state=Car.model)
async def add_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model'] = message.text
    await Car.next()
    await message.reply("Теперь введите год выпуска авто")


async def add_year(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year'] = message.text
    await Car.next()
    await message.reply('Теперь загрузите фото')


async def check_photo(message: types.Message):
    await message.reply('Это не фото!')


async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.photo[-1].file_id
        data['image'] = file_id
    await Car.next()
    await message.reply(text='А теперь введите описание')


# @dp.message_handler(state=Car.description)
async def add_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    pk = await detect_user(message.from_user.username)
    async with state.proxy() as data:
        await sale_car(mark=data['mark'], model=data['model'], year=data['year'],
                       description=data['description'],
                       image=data['image'],
                       pk=pk)
    async with state.proxy() as data:
        await bot.send_photo(message.from_user.id, data['image'],
                             f'Вы добавили авто для продажи:\nмарка: {data["mark"]}\nмодель: {data["model"]}\nгод выпуска: {data["year"]}\nописание: {data["description"]}')
        await bot.send_photo(-1002085281306, data['image'],
                             f'Марка: {data["mark"]}\nМодель: {data["model"]}\nГод выпуска: {data["year"]}\nОписание: {data["description"]}\nНаписать владельцу: @{message.from_user.username}')
        await state.finish()


def register_handlers_sale_car(dp: Dispatcher):
    dp.register_message_handler(add_car, text=['Разместить авто для продажи'], state=None)
    dp.register_message_handler(add_mark, state=Car.mark)
    dp.register_message_handler(add_model, state=Car.model)
    dp.register_message_handler(add_year, state=Car.year)
    dp.register_message_handler(check_photo, lambda message: not message.photo, state=Car.image)
    dp.register_message_handler(add_photo, content_types=['photo'], state=Car.image)
    dp.register_message_handler(add_description, state=Car.description)
