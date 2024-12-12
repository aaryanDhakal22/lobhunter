from ninja import NinjaAPI

from .fetch import *
from .models import Order, PhoneBlockList, AddressBlockList
from pprint import pprint
from .parser import parser
from typing import Callable, List, Dict

api = NinjaAPI()


@api.get("/sync")
def sync_up(request):
    all_messages = fetcher()
    # print("The messages received are " ,all_messages[0]["email_id"])
    blocked = 0
    if len(all_messages) > 0:
        for entry in all_messages:
            order = parser(entry["data"])
            print("\n\nThe order numer is ", order["order_number"])

            # check if phone number is in block list
            if PhoneBlockList.objects.filter(phone=order["phone"]).exists():
                print("Phone number in block list")
                order["blocked"] = True
                blocked += 1

            # check if address is in block list
            elif AddressBlockList.objects.filter(address=order["address"]).exists():
                print("Address in block list")
                order["blocked"] = True
                blocked += 1
            else:
                print("No Blocked")

            blob = {"email_id": entry["email_id"], **order}
            Order.objects.create(**blob)
            print("Order created")
    else:
        print("No messages to add")

    return {"message": "Synced up", "blocked": blocked}


@api.get("/orders")
def orders(request):
    return list(Order.objects.all().values())


@api.get("/order/detail/{order_id}")
def order(request, order_id: int):
    order_data = Order.objects.filter(order_number=order_id).values()[0]
    return order_data


@api.get("/order/date/{date}")
def order_on_date(request, date: str):
    order_data = Order.objects.filter(date=date).values()[0]

    return order_data
