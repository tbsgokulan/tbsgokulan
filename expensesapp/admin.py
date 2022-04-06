from django.contrib import admin

from expensesapp.models import Expenses, Expenses_category

# Register your models here.
admin.site.register(Expenses_category)
admin.site.register(Expenses)
