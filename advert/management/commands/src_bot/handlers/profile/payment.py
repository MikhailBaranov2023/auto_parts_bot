from aiogram import types
from aiogram import Dispatcher
from user.payment import create_payment, check_status_payment
from user.services import add_subscription, check_subscription, check_user
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from django.conf import settings

bot = settings.BOT
dp = settings.DP


# dp.message_handlers(text=['Подписаться'])
async def create_subscription(message: types.Message):
    if await check_user(message.from_user.username) is True:
        if await check_subscription(message.from_user.username) is False:
            await message.reply(
                "Подписка оформляется на 1 месяц, стоимость подписки равна 1000р. По истечению срока подписки вам придет уведомление, чтобы продолжить подписку вам необходимо будет офрмить ее заново. Для того чтобы оформить подписку сейчас нажмите 'Подтвердить'")
            response = await create_payment()
            keyboard = InlineKeyboardMarkup()
            button = InlineKeyboardButton(text="Перейти к оплате", url=response[0])
            keyboard.add(button)
            await bot.send_message(message.from_user.id, "Для оплаты подписки нажмите перейдите по ссылке нижу",
                                   reply_markup=keyboard)
            if await check_status_payment(response[1]) is True:
                await message.answer('Оплата прошла успешно')
                await message.answer(
                    'В близжайщее вреям с вами свяжется админиитратор, для того чтобы подробнее рассказать о функционале бота')
                await message.answer(
                    f"Ваша подписка активна до {await add_subscription(message.from_user.username)}")
            else:
                await message.answer('Оплата не прошла')
        else:
            await bot.send_message(message.from_user.id,
                                   "Вы уже подписаны, чтобы узнать подробную информацию перейдите в раздел 'Информация о профиле'")

    else:
        await message.reply("Вы еще не зарегистрированы, чтобы исправить это нажмите 'Создать профиль'")


def register_handlers_for_subscription(dp: Dispatcher):
    dp.register_message_handler(create_subscription, text=['Подписаться'])
