from rest_framework import serializers
from .models import Sales_return, Sales_return_detail, Sales_return_payment_status
from people.models import Customer
from productapp.models import Product
from settingsapp.models import Warehouse
class Warehouse_serializer_all(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields=['warehouse_name']
class Customer_serializer_all(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['customer_name']
class Sr_serializer(serializers.ModelSerializer):
    sr_warehouse=Warehouse_serializer_all().get_fields().get("warehouse_name")
    sr_customer=Customer_serializer_all().get_fields().get("customer_name")
    class Meta:
        model=Sales_return
        fields=['id','sr_warehouse','sr_customer','sr_date','sr_status',
        'sr_payment_status','sr_paid','sr_due','sr_grand_total','sr_reference']
class sr_product_code_serializers(serializers.ModelSerializer):
     class Meta:
        model =Product
        fields =['product_name','product_code']

class Sr_serializer_detail_edit(serializers.ModelSerializer):
    sr_product_code=sr_product_code_serializers()
    class Meta:
        model=Sales_return_detail
        fields='__all__'
       
class Sr_serializer_header(serializers.ModelSerializer):
    sr_sales=Sr_serializer_detail_edit(many=True)
    sr_warehouse=Warehouse_serializer_all().get_fields().get("warehouse_name")
    sr_customer=Customer_serializer_all().get_fields().get("customer_name")
    class Meta:
        model=Sales_return
        fields='__all__'
class Sr_payment_status_serializer(serializers.ModelSerializer):
    class Meta:
        model=Sales_return_payment_status
        fields='__all__'
       