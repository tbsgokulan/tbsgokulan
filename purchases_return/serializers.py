from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from productapp.models import Product
from people.models import Supplier
from settingsapp.models import Warehouse
from .models import Purchases_return, Purchases_return_purchase_detail, payment_status

class Supplier_serializers(serializers.ModelSerializer):
    class Meta:
        model =Supplier
        fields =['supplier_name']
class Warehouse_serializers(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields=['warehouse_name']

class Purchase_return_serializer(serializers.ModelSerializer):
   
    purchases_return_warehouse=Warehouse_serializers().get_fields().get("warehouse_name")
    purchases_return_supplier=Supplier_serializers().get_fields().get("supplier_name")
    class Meta:
        model = Purchases_return
        fields = ['id','purchases_return_date','purchases_return_reference', 'purchases_return_supplier',
         'purchases_return_warehouse','purchases_return_grand_total','purchases_return_status',
         'purchases_return_paid','purchases_return_due','purchases_return_payment_status']

class product_code_serializers(serializers.ModelSerializer):

    class Meta:
        model =Product
        fields =['product_name','product_code']
class pr_detail_serializer(serializers.ModelSerializer):
    purchases_return_product_code=product_code_serializers()
    class Meta:
        model=Purchases_return_purchase_detail
        fields='__all__'
class Purchase_return_serializer_Header(serializers.ModelSerializer):
    purchases_return_purchase=pr_detail_serializer(read_only=True, many=True)
    purchases_return_warehouse=Warehouse_serializers().get_fields().get("warehouse_name")
    purchases_return_supplier=Supplier_serializers().get_fields().get("supplier_name")
    class Meta:
        model=Purchases_return
        fields='__all__'

class Pr_Payment_serializers(serializers.ModelSerializer):
    class Meta:
        model=payment_status
        fields=['pr_payment_date','pr_payment_reference','pr_payment_choice','pr_payment_amount']