from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from advert.management.commands.src_bot.keyboards.keyboards import confirm_menu, confirm_phone_menu, profile_menu
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from user.services import create_user, check_user, user_info
from django.conf import settings

bot = settings.BOT
dp = settings.DP


class Client(StatesGroup):
    username = State()
    first_name = State()
    last_name = State()
    phone = State()


# @dp.message_handlers(text=['Информация о профиле'])
async def get_info_client(message: types.Message):
    await message.reply(await user_info(message.from_user.username), reply_markup=profile_menu)


# @dp.message_handler(text=['Создать профиль'], state=None)
async def create_profile(message: types.Message):
    if await check_user(message.from_user.username) is False:
        await Client.username.set()
        await message.reply('Для создания профиля неоходимо использовать ваш username', reply_markup=confirm_menu)
    else:
        await message.reply('Вы уже зарегистрированы')


# @dp.message_handler(state=Client.username)
async def add_username(message: types.Message, state: FSMContext):
    if message.text == 'Подтвердить':
        async with state.proxy() as data:
            data['username'] = message.from_user.username
            await Client.next()
        await message.reply('Добавьте имя')
    elif message.text == 'Отменить':
        await state.finish()


# @dp.message_handler(state=Client.first_name)
async def add_first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
        await Client.next()
    await message.reply('Теперь введите фамилию')


# @dp.message_handler(state=Client.last_name)
async def add_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
        await Client.next()
    await message.reply('Разрешите использвать ваш номер телефона?', reply_markup=confirm_phone_menu)


# @dp.message_handler(state=Client.phone)
async def add_phone(message: types.ContentType.CONTACT, state: FSMContext):
    if message.contact is not None:
        async with state.proxy() as data:
            data['phone'] = message.contact.phone_number
        async with state.proxy() as data:
            await create_user(data['username'], data['first_name'], data['last_name'], data['phone'])
            await message.reply(f"""
                Ваш профиль создан, проверьте ваши данные
                username - {data['username']},
                имя - {data['first_name']},
                Фамилия - {data['last_name']},
                Телефон - {data['phone']}
                """)
        await state.finish()
    elif message.contact is None:
        await state.finish()


def register_handlers_add_client(dp: Dispatcher):
    dp.register_message_handler(create_profile, text=['Создать профиль'], state=None)
    dp.register_message_handler(add_username, state=Client.username),
    dp.register_message_handler(add_first_name, state=Client.first_name),
    dp.register_message_handler(add_last_name, state=Client.last_name),
    dp.register_message_handler(add_phone, state=Client.phone, content_types=['contact'])
    dp.register_message_handler(get_info_client, text=['Информация о профиле'])
