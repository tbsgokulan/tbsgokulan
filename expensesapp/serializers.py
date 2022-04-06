from dataclasses import field
from rest_framework import serializers
from settingsapp.models import Warehouse

from expensesapp.models import Expenses, Expenses_category
class Expenses_category_serializer(serializers.ModelSerializer):
    class Meta:
        model=Expenses_category
        fields='__all__'
class value__expensescategory_serializer(serializers.ModelSerializer):
    class Meta:
        model=Expenses_category
        fields=['expenses_category_name']
class value_expenses_warehouse_serializer(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields=['warehouse_name']

class Expenses_serializer(serializers.ModelSerializer):
    expensescategory=value__expensescategory_serializer().get_fields().get("expenses_category_name")
    expenses_warehouse=value_expenses_warehouse_serializer().get_fields().get("warehouse_name")
    class Meta:
        model=Expenses
        fields='__all__'