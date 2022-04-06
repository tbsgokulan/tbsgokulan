from django.contrib import admin
from .models import Purchases_return, Purchases_return_purchase_detail, payment_status

# Register your models here.
admin.site.register(Purchases_return)
admin.site.register(Purchases_return_purchase_detail)
admin.site.register(payment_status)