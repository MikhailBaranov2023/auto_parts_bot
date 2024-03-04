from advert.models import Car, Request, Request_To_Repair
from asgiref.sync import sync_to_async

"""добавление авто на продажу"""


@sync_to_async
def sale_car(mark, model, description, year, image, pk):
    Car.objects.create(
        mark=mark,
        model=model,
        description=description,
        year=year,
        image=image,
        owner_id=pk,
        sale=True
    )


"""добавление авто в разборе"""


@sync_to_async
def sale_parts_car(mark, model, description, year, pk):
    Car.objects.create(
        mark=mark,
        model=model,
        description=description,
        owner_id=pk,
        year=year,
        disassembly=True
    )


"""создание запроса на запчасть"""


@sync_to_async
def create_request_to_parts(mark_auto, model_auto, year_auto, description, pk):
    Request.objects.create(
        mark_auto=mark_auto,
        model_auto=model_auto,
        year_auto=year_auto,
        description=description,
        part=True,
        owner_id=pk
    )


"""создание запроса на агрегат"""


@sync_to_async
def create_request_to_unit(mark_auto, model_auto, year_auto, description, pk):
    Request.objects.create(
        mark_auto=mark_auto,
        model_auto=model_auto,
        year_auto=year_auto,
        description=description,
        unit=True,
        owner_id=pk
    )


@sync_to_async
def create_requests_to_repair(country, city, description, pk):
    Request_To_Repair.objects.create(
        country=country,
        city=city,
        description=description,
        owner_id=pk
    )


@sync_to_async
def detect_my_requests_to_parts(pk):
    if Request.objects.filter(owner_id=pk, part=True).exists() is True:
        requests_to_part = Request.objects.filter(owner_id=pk, part=True)
        part_list = ["Запросы на запчасти", ]
        for p in requests_to_part:
            part_list.append(
                f"Марка - {p.mark_auto}, Модель - {p.model_auto}, Год выпуска авто - {p.year_auto}, Описание - {p.description}")
        return '\n'.join(part_list)
    return 'У вас нет звапросов на запчастит'


@sync_to_async
def detect_my_requests_to_unit(pk):
    if Request.objects.filter(owner_id=pk, unit=True).exists() is True:
        requests_to_unit = Request.objects.filter(owner_id=pk, unit=True)
        unit_list = ["Запросы на агрегат", ]
        for u in requests_to_unit:
            unit_list.append(
                f"Марка - {u.mark_auto}, Модель - {u.model_auto}, Год выпуска авто - {u.year_auto}, Описание - {u.description}"
            )
        return '\n'.join(unit_list)
    return 'У вас нет запросов на агрегат'


@sync_to_async
def detect_my_requests_to_repair(pk):
    if Request_To_Repair.objects.filter(owner_id=pk).exists() is True:
        my_requests = Request_To_Repair.objects.filter(owner_id=pk)
        req_list = ['Запросы на ремонт']
        for r in my_requests:
            req_list.append(
                f"Страна - {r.country}, Город - {r.city}, Описание - {r.description}"
            )
        return '\n'.join(req_list)
    return 'У вас нет запросов на ремонт'


@sync_to_async
def detect_my_cars_to_sale(pk):
    if Car.objects.filter(owner_id=pk, sale=True).exists() is True:
        my_cars_to_sale = Car.objects.filter(owner_id=pk, sale=True)
        car_list = []
        for car in my_cars_to_sale:
            car_list.append(
                f"Марка - {car.mark}, Модель - {car.model}, Описание - {car.description}")
        return '\n'.join(car_list)
    return "У вас нет авто для прdодажи"


@sync_to_async
def detect_my_cars_to_parts(pk):
    if Car.objects.filter(owner_id=pk, disassembly=True).exists() is True:
        my_cars = Car.objects.filter(owner_id=pk, disassembly=True)
        car_list = []
        for car in my_cars:
            car_list.append(f"Марка - {car.mark}, Модель - {car.model}, Описание - {car.description}")
        return '\n'.join(car_list)
    return "У вас нет авто в разборе "
