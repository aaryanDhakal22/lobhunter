from django.db import models


# Create your models here.
class Order(models.Model):
    email_id = models.CharField(max_length=20)
    order_number = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    date = models.DateField()
    phone = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=5)
    ticket = models.CharField(max_length=10000)
    address = models.CharField(max_length=30, null=True)
    time = models.TimeField(default="00:00:00")
    blocked = models.BooleanField(default=False)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"Order {self.order_number} by {self.customer_name}"


class PhoneBlockList(models.Model):
    phone = models.IntegerField()
    reason = models.CharField(max_length=1000, default="", blank=True)


class AddressBlockList(models.Model):
    address = models.CharField(max_length=30)
    reason = models.CharField(max_length=1000, default="", blank=True)
