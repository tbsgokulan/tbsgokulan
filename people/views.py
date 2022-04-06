from django.db.models import manager, query
from django.shortcuts import render
from .models import Customer,Supplier
from .serializers import Customer_serializer,Supplier_serializer
from rest_framework.views import APIView
from rest_framework import serializers,status
from rest_framework.response import Response
import traceback
# Create your views here.
class list_customer(APIView):
    def get(self,request):
        query=Customer.objects.filter(active=True)
        serializer_class=Customer_serializer(query,many=True)
        return Response(serializer_class.data)
    def post(self,request):
        try:
            data=request.data
            customer=Customer.objects.create(
            customer_name=data['customer_name'],
            customer_email=data['customer_email'],
            customer_phone_no=data['customer_phone_no'],
            customer_country=data['customer_country'],
            customer_city=data['customer_city'],
            customer_address=data['customer_address'])
            return Response({"result":"created"},status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(),status=status.HTTP_400_BAD_REQUEST)

class detailed_customer(APIView):
    # def get(self,request,cid):
    #     query=customer.objects.filter(id=cid)
    #     serializer_class=customer_serializer(query,many=True)
    #     return Response(serializer_class.data)
    def put(self,request,cid):
        try:
            customer_obj=Customer.objects.get(id=cid)
            serializer_obj=Customer_serializer(customer_obj,data=request.data)
            if serializer_obj.is_valid(raise_exception=True):
                save_customer=serializer_obj.save()
                return Response({"result":"updated"},status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,cid):
        customer_obj=Customer.objects.filter(id=cid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)

    #crud in supplier

class list_supplier(APIView):
    def get(self,request):
        query=Supplier.objects.filter(active=True)
        serializer_class=Supplier_serializer(query,many=True)
        return Response(serializer_class.data)
    def post(self,request):
        try:
            data=request.data
            supplier=Supplier.objects.create(
            supplier_name=data['supplier_name'],
            supplier_email=data['supplier_email'],
            supplier_phone_no=data['supplier_phone_no'],
            supplier_country=data['supplier_country'],
            supplier_city=data['supplier_city'],
            supplier_address=data['supplier_address'])
            return Response({"result":"created"},status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(),status=status.HTTP_400_BAD_REQUEST)

class detailed_supplier(APIView):
    # def get(self,request,sid):
    #     query=supplier.objects.filter(id=sid)
    #     serializer_class=supplier_serializer(query,many=True)
    #     return Response(serializer_class.data)
    def put(self,request,sid):
        try:
            supplier_obj=Supplier.objects.get(id=sid)
            serializer_obj=Supplier_serializer(supplier_obj,data=request.data)
            if serializer_obj.is_valid(raise_exception=True):
                save_supplier=serializer_obj.save()
                return Response({"result":"updated"},status=status.HTTP_200_OK)
        except Exception:
            return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,sid):
        supplier_obj=Supplier.objects.filter(id=sid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)