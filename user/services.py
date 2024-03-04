from user.models import User
from asgiref.sync import sync_to_async
from datetime import date, timedelta
import calendar


@sync_to_async
def create_user(username, first_name, last_name, phone):
    User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        phone=phone
    )


@sync_to_async
def check_user(username):
    if User.objects.filter(username=username).exists():
        return True
    return False


@sync_to_async
def user_info(username):
    if User.objects.filter(username=username).exists() is True:
        if User.objects.get(username=username).subscription is True:
            subscription = f'Подписка активна до - {User.objects.get(username=username).date_to}'
        else:
            subscription = 'Подписка не активна, хотите оформить подписку?'
        return f"""
        Ваш профиль :
        Имя пользователя - {User.objects.get(username=username).username},
        Имя - {User.objects.get(username=username).first_name},
        Фамилия - {User.objects.get(username=username).last_name},
        Телефон - {User.objects.get(username=username).phone},
        Статус подписки - {subscription}
        """
    return "Вы не зарегистрированы, чтобы зарегистрироваться выберите пункт меню 'Создать профиль'"


@sync_to_async
def detect_user(username):
    if User.objects.filter(username=username).exists() is True:
        return User.objects.get(username=username).pk
    return None


@sync_to_async
def add_subscription(username):
    today = date.today()
    days = calendar.monthrange(today.year, today.month)[1]
    next_month_date = today + timedelta(days=days)
    User.objects.filter(username=username).update(subscription=True, date_from=date.today(), date_to=next_month_date)
    return next_month_date


@sync_to_async
def check_subscription(username):
    if User.objects.get(username=username).subscription is True:
        return True
    return False
