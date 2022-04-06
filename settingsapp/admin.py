from django.contrib import admin
from.models import Category,Warehouse, Brand,Unit, Warehouse_detail

# Register your models here.
admin.site.register(Warehouse)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Unit)
admin.site.register(Warehouse_detail)