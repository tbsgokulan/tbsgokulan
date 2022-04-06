from dataclasses import field
from pyexpat import model
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from settingsapp.models import Brand, Category, Unit
from . models import Product

class Unit_serializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ['unit_name']
class Brand_serializer(serializers.ModelSerializer):

    class Meta:
        model= Brand
        fields =['brand_name']
class Catergory_serializer(serializers.ModelSerializer):

    class Meta:
        model =Category
        fields =['category_name']
class Product_serializer(serializers.ModelSerializer):

    purchase_unit = Unit_serializer()
    category= Catergory_serializer()
    brand = Brand_serializer()
    product_unit=Unit_serializer()
    sale_unit=Unit_serializer()
    class Meta:
        model=Product
        fields='__all__'


class ProductunitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = '__all__'

#get all field in product
class all_field_category_serializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class all_field_brand_serializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
class all_field_unit_serializer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields='__all__'
class all_field_product_serializer(serializers.ModelSerializer):
    
    category= all_field_category_serializer()
    brand = all_field_brand_serializer()
    product_unit=all_field_unit_serializer()
    purchase_unit = all_field_unit_serializer()
    sale_unit=all_field_unit_serializer()
    class Meta:
        model=Product
        fields='__all__'
