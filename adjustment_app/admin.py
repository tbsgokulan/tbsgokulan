from django.contrib import admin

from .models import Adjustment, Adjustment_detail

# Register your models here.
admin.site.register(Adjustment)
admin.site.register(Adjustment_detail)
