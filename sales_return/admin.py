from atexit import register
from django.contrib import admin
from .models import Sales_return, Sales_return_detail, Sales_return_payment_status

# Register your models here.
admin.site.register(Sales_return)
admin.site.register(Sales_return_detail)
admin.site.register(Sales_return_payment_status)