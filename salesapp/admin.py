from django.contrib import admin

from salesapp.models import Sales, Sales_detail, Sales_payment_status

# Register your models here.
admin.site.register(Sales)
admin.site.register(Sales_detail)
admin.site.register(Sales_payment_status)
