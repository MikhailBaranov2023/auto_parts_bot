from django.conf import settings
from aiogram import executor
from advert.management.commands.src_bot.handlers.services.add_menu import register_handlers_for_menu
from advert.management.commands.src_bot.handlers.sale_auto.add_car import register_handlers_sale_car
from advert.management.commands.src_bot.handlers.sale_auto.sale_car_to_parts import register_handlers_sale_parts_car
from advert.management.commands.src_bot.handlers.profile.client import register_handlers_add_client
from advert.management.commands.src_bot.handlers.requests.add_request_to_parts import \
    register_handlers_add_request_to_part
from advert.management.commands.src_bot.handlers.requests.add_request_to_unit import \
    register_handlers_add_request_to_unit
from advert.management.commands.src_bot.handlers.requests.add_request_to_repair import \
    register_handlers_add_request_to_repair
from advert.management.commands.src_bot.handlers.sale_auto.my_cars import register_handlers_my_cars
from advert.management.commands.src_bot.handlers.requests.my_requests import register_handlers_my_requests
from advert.management.commands.src_bot.handlers.sale_auto.to_group import register_handler_to_group
from advert.management.commands.src_bot.handlers.profile.payment import register_handlers_for_subscription
from advert.management.commands.src_bot.handlers.services.cancel_handler import register_cancel_handlers

bot = settings.BOT
dp = settings.DP


class Command:

    async def on_startup(_):
        print('Бот вышел  в онлайн')

    register_cancel_handlers(dp)
    register_handlers_for_subscription(dp)
    register_handler_to_group(dp)
    register_handlers_my_cars(dp)
    register_handlers_my_requests(dp)
    register_handlers_sale_car(dp)
    register_handlers_sale_parts_car(dp)
    register_handlers_add_client(dp)
    register_handlers_add_request_to_repair(dp)
    register_handlers_add_request_to_part(dp)
    register_handlers_add_request_to_unit(dp)
    register_handlers_for_menu(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
