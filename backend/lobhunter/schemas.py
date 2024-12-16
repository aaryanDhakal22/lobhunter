from ninja import ModelSchema, Schema
from lobhunter.models import Order
from typing import List


class OrderSchema(ModelSchema):
    class Meta:
        model = Order
        fields = "__all__"


class OrderPayloadSchema(Schema):
    order_number: int
    total: float
    customer_name: str


class OrderResponse(Schema):
    success: bool
    message: str
    payload: List[OrderPayloadSchema]
