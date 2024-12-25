import google.auth.transport.requests
from ninja import NinjaAPI

from lobhunter.schemas import (
    BlockList,
    OrderPayloadSchema,
    OrderResponse,
    OrderSchema,
    StatusPayloadSchema,
)
from .fetch import *
from .models import Order, PhoneBlockList, AddressBlockList
from pprint import pprint
from .parser import parser
from typing import Callable, List, Dict

api = NinjaAPI()


@api.get("/sync")
def sync_up(request):
    print("Starting Syncronization")
    all_messages = fetcher()
    print(f"Adding{len(all_messages)} to the database")
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
            elif AddressBlockList.objects.filter(
                address=order["address"].upper()
            ).exists():
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


@api.get("/order/date/{date}", response=OrderResponse)
def order_on_date(request, date: str):
    print(date)
    order_data = Order.objects.filter(date=date).values(
        "order_number", "total", "customer_name"
    )
    payload = [
        OrderPayloadSchema(
            order_number=order["order_number"],
            total=order["total"],
            customer_name=order["customer_name"],
        )
        for order in order_data
    ]

    return {
        "success": True,
        "message": "Orders retrieved successfully",
        "payload": payload,
    }


@api.get("/blocklist/blocks", response=List[str])
def all_blocks(request):
    phones = [str(i.phone) for i in PhoneBlockList.objects.all()]
    address = [str(i.address) for i in AddressBlockList.objects.all()]
    blocks = phones + address
    print(blocks)
    return blocks


@api.post("/blocklist/add")
def add_to_blocklist(request, data: BlockList):
    print(data)
    print(data.address)
    print(data.phone)
    message = ""
    if len(data.phone) > 1:
        PhoneBlockList.objects.create(data.phone)
        message += "1 phone number was blocked \n"

    if len(data.address) > 1:
        AddressBlockList.objects.create(address=data.address.upper())
        message += "1 address was blocked \n"

    return {"message": message}


@api.put("/order/status/")
def change_status(request, payload: StatusPayloadSchema):
    chosen = Order.objects.get(pk=payload.order_number)
    chosen.status = payload.status
    chosen.save()
    return {"message": "Status was changed"}
