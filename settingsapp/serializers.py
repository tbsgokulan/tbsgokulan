from django.db.models import fields
from rest_framework import serializers
from .models import Brand, Unit, Warehouse,Category, Warehouse_detail

class Warehouse_serializer(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields='__all__'

class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class Brand_serializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
        
class Units_serializer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields='__all__' 
