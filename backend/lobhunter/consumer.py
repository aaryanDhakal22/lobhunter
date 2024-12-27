import json
from channels.generic.websocket import AsyncWebsocketConsumer
from lobhunter.parser import kitchen_ticket_number
from .models import Order
from channels.db import database_sync_to_async
from bs4 import BeautifulSoup


class OrderConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = "kitchen_group"
        print("\n\n", self.channel_name, " is connected")
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        print("Message Received", message)
        await self.channel_layer.group_send(
            self.group_name, {"type": "broadcast_message", "message": message}
        )

    @database_sync_to_async
    def get_order(self, message):
        return Order.objects.filter(order_number=message).first()

    def kitchen_ticket(self, string):
        soup = BeautifulSoup(string, "html.parser")
        table_tags = soup.find_all("table")
        if table_tags:
            return str(table_tags[1])
        else:
            return None

    async def broadcast_message(self, event):
        message = int(event["message"])
        order = await self.get_order(message)
        await self.send(
            text_data=json.dumps(
                {
                    "ticket": self.kitchen_ticket(order.ticket),
                    "kitchenNumber": order.kitchen_number,
                }
            )
        )
