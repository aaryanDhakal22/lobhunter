from ninja import NinjaAPI

from .fetch import *
from .models import Order, PhoneBlockList, AddressBlockList
from pprint import pprint
from .parser import parser
from typing import Callable, List, Dict

api = NinjaAPI()

def default_fetcher() -> List[Dict]:
    """Default fetcher for production."""
    from .fetch import fetcher

    return fetcher()


@api.get("/sync")
def sync_up(request, fetcher: Callable = default_fetcher):
    all_messages = fetcher()
    if all_messages:
        for entry in all_messages:
            # if Order.objects.filter(email_id=entry["email_id"]).exists():
            #     print("Order already exists")
            #     continue
            order = parser(entry["data"])
            # check if phone number is in block list
            if PhoneBlockList.objects.filter(phone=order["phone"]).exists():
                print("Phone number in block list")
                return {
                    "message": "Phone number in block list",
                    "order_number": order["order_number"],
                }
            # check if address is in block list
            if AddressBlockList.objects.filter(address=order["address"]).exists():
                print("Address in block list")
                return {
                    "message": "Address in block list",
                    "order_number": order["order_number"],
                }
            blob = {"email_id": entry["email_id"], **order}
            Order.objects.create(**blob)
            print("Order created")
        return {"message": "Synced up"}


@api.get("/orders")
def orders(request):
    return list(Order.objects.all().values())


@api.get("/order/{order_id}")
def order(request, order_id: int):
    order_data = Order.objects.filter(order_number=order_id).values()
    return list(order_data)


@api.get("/order/{date}")
def order_on_date(request, date: str):
    order_data = Order.objects.filter(date=date).values()
    return list(order_data)
