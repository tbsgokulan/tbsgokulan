from rest_framework import serializers
from people.models import Customer
from productapp.models import Product

from salesapp.models import Sales, Sales_detail, Sales_payment_status
from settingsapp.models import Warehouse
class Warehouse_serializer_all(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields=['warehouse_name']
class Customer_serializer_all(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['customer_name']
class Sales_serializer(serializers.ModelSerializer):
    sales_warehouse=Warehouse_serializer_all().get_fields().get("warehouse_name")
    sales_customer=Customer_serializer_all().get_fields().get("customer_name")
    class Meta:
        model=Sales
        fields=['id','sales_warehouse','sales_customer','sales_date','sales_status',
        'sales_payment_status','sales_paid','sales_due','sales_grand_total','sales_reference']
class product_code_serializers(serializers.ModelSerializer):
     class Meta:
        model =Product
        fields =['product_name','product_code']

class Sales_serializer_detail_edit(serializers.ModelSerializer):
    sales_product_code=product_code_serializers()
    class Meta:
        model=Sales_detail
        fields='__all__'
       
class Sales_serializer_header(serializers.ModelSerializer):
    sales_sales=Sales_serializer_detail_edit(many=True)
    sales_warehouse=Warehouse_serializer_all().get_fields().get("warehouse_name")
    sales_customer=Customer_serializer_all().get_fields().get("customer_name")
    class Meta:
        model=Sales
        fields='__all__'
class Sales_payment_status_serializer(serializers.ModelSerializer):
    class Meta:
        model=Sales_payment_status
        fields='__all__'
       