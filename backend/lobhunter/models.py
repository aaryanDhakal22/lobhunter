from datetime import datetime

import pytz
from django.db import models


# Create your models here.
class Order(models.Model):
    email_id = models.CharField(max_length=20)
    kitchen_number = models.BigIntegerField(help_text="Kitchen ticket number - changed to BigIntegerField to handle large numbers")
    order_number = models.BigIntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    date = models.DateField()
    phone = models.BigIntegerField(help_text="Phone number - changed to BigIntegerField to handle large phone numbers")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=5)
    ticket = models.CharField(max_length=10000)
    address = models.CharField(max_length=30, null=True)
    time = models.TimeField(default="00:00:00")
    blocked = models.BooleanField(default=False)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"Order {self.order_number} by {self.customer_name}"


class OperationDate(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    counter = models.IntegerField()
    # @property
    # def now_date_and_time(self):
    #     now_utc = datetime.now(pytz.utc)
    #     eastern = pytz.timezone("US/Eastern")
    #     now_est = now_utc.astimezone(eastern)
    #     return now_est.strftime("%Y-%m-%d %H:%M:%S")


class PhoneBlockList(models.Model):
    phone = models.BigIntegerField(help_text="Phone number - changed to BigIntegerField to handle large phone numbers")
    reason = models.CharField(max_length=1000, default="", blank=True)


class AddressBlockList(models.Model):
    address = models.CharField(max_length=30)
    reason = models.CharField(max_length=1000, default="", blank=True)
