from ninja import ModelSchema
from lobhunter.models import Order

class OrderSchema(ModelSchema):
    class Meta:
        model = Order
        fields = "__all__"