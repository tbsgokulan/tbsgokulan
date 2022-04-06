from django.contrib import admin

from purchasesapp.models import Purchase, payment_status, purchase_detail

# Register your models here.
admin.site.register(Purchase)
admin.site.register(purchase_detail)
admin.site.register(payment_status)
