from dataclasses import field
from rest_framework import serializers
from productapp.models import Product

from settingsapp.models import Warehouse, Warehouse_detail
from .models import Transfer
class prd_code_serializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["product_code"]
class Warehouse_query(serializers.ModelSerializer):
    product_code=prd_code_serializer()
    class Meta:
        model=Warehouse_detail
        fields='__all__'
class Warehouse_serializers_tr(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields=['warehouse_name']

class transfer_list(serializers.ModelSerializer):
    tr_from_warehouse=Warehouse_serializers_tr().get_fields().get("warehouse_name")
    tr_to_warehouse=Warehouse_serializers_tr().get_fields().get("warehouse_name")
    class Meta:
        model=Transfer
        fields='__all__'