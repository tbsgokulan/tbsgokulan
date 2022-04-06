from sys import api_version
import traceback
from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from settingsapp.models import Brand, Category,Unit
from productapp.models import Product
from settingsapp.models import Unit
from .serializers import Product_serializer, ProductunitSerializer, Unit_serializer, all_field_product_serializer


# Create your views here.
# class sale_unit(APIView):
#     def get(self,request,uid):
#         query=unit.objects.filter(id=uid).values() 
class list_product(APIView):
    def get(self,request):
        query=Product.objects.filter(active=True)
        serializer_class=all_field_product_serializer(query,many=True)
        return Response(serializer_class.data)
    def post(self,request):
        try:
            data=request.data            
            product=Product.objects.create(
            product_name=data['product_name'],
            product_code=data['product_code'],
            category=Category.objects.get(id=data['category']),
            brand=Brand.objects.get(id=data['brand']),
            barcode_symbology=data['barcode_symbology'],
            product_cost=data['product_cost'],
            product_price=data['product_price'],
            product_unit=Unit.objects.get(id=data['product_unit']),
            sale_unit=Unit.objects.get(id=data['sale_unit']),
            purchase_unit=Unit.objects.get(id=data['purchase_unit']),
            stock_alert=data['stock_alert'],
            order_tax=data['order_tax'],
            tax_type=data['tax_type'],
            note=data['note'],
            product_image=data['product_image'])
             
            return Response({"result":"created"},status=status.HTTP_201_CREATED)  
        except Exception:
            return Response(traceback.format_exc(),status=status.HTTP_400_BAD_REQUEST)
    # def post(self,request):
    #     try:
    #         serializer_obj=product_serializer(data=request.data)
    #         if serializer_obj.is_valid(raise_exception=True):
    #             product_save=serializer_obj.save()
    #             return Response({"result":"created"},status=status.HTTP_201_CREATED)
    #     except Exception:
    #         return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
class detailed_product(APIView):
    # def put(self,request,pid):
    #     try:
    #         product_obj=Product.objects.get(id=pid)
    #         serializer_obj=Product_serializer(product_obj,data=request.data)
    #         if serializer_obj.is_valid(raise_exception=True):
    #             product_save=serializer_obj.save()
    #             return Response({"result":"updated"},status=status.HTTP_200_OK)
    #     except Exception:
    #         return Response (serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,pid):
        data=request.data
        update_method=Product.objects.filter(id=pid).update( product_name=data['product_name'],
            product_code=data['product_code'],
            category=Category.objects.get(id=data['category']),
            brand=Brand.objects.get(id=data['brand']),
            barcode_symbology=data['barcode_symbology'],
            product_cost=data['product_cost'],
            product_price=data['product_price'],
            product_unit=Unit.objects.get(id=data['product_unit']),
            sale_unit=Unit.objects.get(id=data['sale_unit']),
            purchase_unit=Unit.objects.get(id=data['purchase_unit']),
            stock_alert=data['stock_alert'],
            order_tax=data['order_tax'],
            tax_type=data['tax_type'],
            note=data['note'],
            product_image=data['product_image'])
        return Response ({"result":"updated"},status=status.HTTP_200_OK)
    def delete(self,request,pid):
        product_obj=Product.objects.filter(id=pid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)


class demounit(APIView):

    def get(self, request, id):
        
        # x=[]
        # unit = Unit.objects.get(id=id)
        # serializer = Unit_serializer(unit)
        # x.append(serializer.data)
        unit_get = Unit.objects.filter(id=id).values('unit_name')
        print(unit_get)
        for i in unit_get:
            print(i['unit_name'])
        units = Unit.objects.filter(base_unit=i['unit_name'],active=True)
        serializer = ProductunitSerializer(units,many=True)
        return Response(serializer.data)
        # return Response(x)


class unitfilter(APIView):

    def get(self, request):

        unit = Unit.objects.filter(active=True)
        serializer= ProductunitSerializer(unit,many=True)
        return Response(serializer.data)