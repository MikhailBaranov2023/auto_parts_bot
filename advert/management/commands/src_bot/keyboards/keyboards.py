from aiogram import types

"""main menu"""
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(types.KeyboardButton('Объявления'), types.KeyboardButton('Создать запрос'),
              types.KeyboardButton('Профиль'))

btn_for_back = types.KeyboardButton('Назад')

"""меню объявление"""
btn_cars = types.KeyboardButton('Продать авто')
btn_disassembly = types.KeyboardButton('Авто в разборе')
advert_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
advert_menu.add(btn_cars, btn_disassembly, btn_for_back)

"""меню запрос"""
btn_unit = types.KeyboardButton('Запрос на агрегат')
btn_part = types.KeyboardButton('Запрос на запчасть')
btn_repair = types.KeyboardButton('Запрос на ремонт')
btn_my_requests = types.KeyboardButton('Мои запросы')
request_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
request_menu.add(btn_unit, btn_part, btn_repair, btn_my_requests, btn_for_back)

"меню подвердить"
btn_yes = types.KeyboardButton('Подтвердить')
btn_no = types.KeyboardButton('Отменить')
confirm_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
confirm_menu.add(btn_yes, btn_no)

"меню профиль"
btn_my_profile = types.KeyboardButton('Информация о профиле')
btn_create = types.KeyboardButton('Создать профиль')
btn_subscription = types.KeyboardButton('Подписаться')
profile_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
profile_menu.add(btn_my_profile, btn_subscription, btn_create, btn_for_back)

"подтвердить передачу номер телефона"
btn_yes = types.KeyboardButton('Поделиться номером', request_contact=True)
btn_no = types.KeyboardButton('Отменить')
confirm_phone_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
confirm_phone_menu.add(btn_yes, btn_no)

"Меню продать авто"
btn_fiend_auto = types.KeyboardButton('Поиск по авто')
btn_sale_auto = types.KeyboardButton('Разместить авто для продажи')
btn_my_auto = types.KeyboardButton('Мои авто на продаже')
sale_auto_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
sale_auto_menu.add(btn_fiend_auto, btn_sale_auto, btn_my_auto, btn_for_back)

"Меню авто в разборе"
btn_fiend_auto_to_parts = types.KeyboardButton('Поиск по авто в разборе')
btn_auto_to_parts = types.KeyboardButton('Разместить авто в разборе')
btn_my_auto_to_parts = types.KeyboardButton('Мои авто в разборе')
cars_to_parts_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
cars_to_parts_menu.add(btn_fiend_auto_to_parts, btn_auto_to_parts, btn_my_auto_to_parts, btn_for_back)
