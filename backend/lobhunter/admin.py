from django.contrib import admin
from .models import AddressBlockList, Order, PhoneBlockList

# Register your models here.
admin.site.register(Order)
admin.site.register(PhoneBlockList)
admin.site.register(AddressBlockList)
