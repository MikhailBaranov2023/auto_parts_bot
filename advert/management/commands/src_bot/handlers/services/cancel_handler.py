from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram import types
from advert.management.commands.src_bot.keyboards.keyboards import main_menu
from django.conf import settings

bot = settings.BOT
dp = settings.DP


# @dp.message_handlers(state='*', text=['назад'], ignore_case=True)
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.reply(message.text, reply_markup=main_menu)
    else:
        await state.finish()
        await message.reply('Вы отменили добавление объекта', reply_markup=main_menu)


def register_cancel_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_handler, state='*', text=['Назад'])
    dp.register_message_handler(cancel_handler, state='*', text=['Отменить'])
