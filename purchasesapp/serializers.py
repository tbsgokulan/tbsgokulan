from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from people.models import Supplier
from productapp.models import Product

from purchasesapp.models import Purchase, payment_status, purchase_detail
from settingsapp.models import Category, Warehouse
class Supplier_serializers(serializers.ModelSerializer):

    class Meta:
        model =Supplier
        fields =['supplier_name']
class Warehouse_serializers(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields=['warehouse_name']

class Purchase_serializer(serializers.ModelSerializer):
   
    warehouse=Warehouse_serializers().get_fields().get("warehouse_name")
    supplier=Supplier_serializers().get_fields().get("supplier_name")
    class Meta:
        model = Purchase
        fields = ['id','date','reference', 'supplier', 'warehouse','grand_total','status','paid','due','payment_status']

class product_code_serializers(serializers.ModelSerializer):

    class Meta:
        model =Product
        fields =['product_name','product_code']
class purchase_detail_serializer(serializers.ModelSerializer):
    product_code=product_code_serializers()
    class Meta:
        model=purchase_detail
        fields='__all__'
class Purchase_serializer_Header(serializers.ModelSerializer):
    Purchase=purchase_detail_serializer(read_only=True, many=True)
    warehouse=Warehouse_serializers().get_fields().get("warehouse_name")
    supplier=Supplier_serializers().get_fields().get("supplier_name")
    class Meta:
        model=Purchase
        fields='__all__'

class Payment_serializers(serializers.ModelSerializer):
    class Meta:
        model=payment_status
        fields=['payment_date','payment_reference','payment_choice','payment_amount']
