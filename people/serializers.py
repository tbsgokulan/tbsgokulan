from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Customer,Supplier

class Customer_serializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
class Supplier_serializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields='__all__'