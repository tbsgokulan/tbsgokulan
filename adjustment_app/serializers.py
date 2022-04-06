from dataclasses import field
from rest_framework import serializers

from settingsapp.models import Warehouse

from .models import Adjustment, Adjustment_detail

class Warehouse_serializer_adj(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields=['warehouse_name']

class Adjustment_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model=Adjustment_detail
        fields='__all__'
class Adjustment_serializer(serializers.ModelSerializer):
    adj_warehouse=Warehouse_serializer_adj().get_fields().get("warehouse_name")
    adj_detail=Adjustment_detail_serializer(many=True)
    class Meta:
        model=Adjustment
        fields='__all__'