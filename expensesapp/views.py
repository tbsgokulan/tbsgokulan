from http.client import OK
from itertools import count
from multiprocessing.dummy import active_children
from telnetlib import STATUS
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
import traceback
from .serializers import Expenses_category_serializer, Expenses_serializer
from settingsapp.models import Warehouse
from .models import Expenses, Expenses_category

# Create your views here.
class Expenses_category_api(APIView):
    def post(self,request):
        try:
            with transaction.atomic():
                data=request.data
                create_expense=Expenses_category.objects.create(
                    expenses_category_name=data['expenses_category_name'],
                    expenses_description=data['expenses_description'])
                return Response({"result":"sucess"},status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(),status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        query=Expenses_category.objects.filter(active=True)
        serializer_class=Expenses_category_serializer(query,many=True)
        return Response(serializer_class.data)
    def put(self,request,pid):
        try:
            obj=Expenses_category.objects.get(id=pid)
            serializer_class=Expenses_category_serializer(obj,data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
            return Response({"result":"updated"},status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,sid):
        query=Expenses_category.objects.filter(id=sid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)


class Create_expenses_api(APIView):
    count=0
    def post(self,request):
        demo=Expenses.objects.all()
        print(demo)
        if demo:
            last_entry=Expenses.objects.latest("created_date")    
            last_reference_entry=last_entry.id
            a=["%04d" % x for x in range(10000)]
            pid=last_reference_entry+1
            value="EXP_{}".format(a[pid])
        else:
            Create_expenses_api.count+=1
            a=["%04d" % x for x in range(10000)]
            id=self.count
            print(id)
            value="EXP_{}".format(a[id])
            print(value)
        try:
            with transaction.atomic():
                data=request.data
                expensescategoryee=Expenses_category.objects.get(id=data["expensescategory"])
                expenses_warehousee=Warehouse.objects.get(id=data["expenses_warehouse"])
                reference=data["expenses_reference"] if data["expenses_reference"] else value
                update_expenses,create_expenses=Expenses.objects.update_or_create(
                    expenses_reference=reference,
                     defaults={"expensescategory":expensescategoryee,
                      "expenses_date":data["expenses_date"],
                    "expenses_detail":data["expenses_detail"],
                    "expenses_amount":data["expenses_amount"],
                    "expenses_warehouse":expenses_warehousee})
                return Response({"result":"sucess"},status=status.HTTP_200_OK)
        except Exception:
                return Response(traceback.format_exc(),status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        query=Expenses.objects.filter(active=True)
        serializer_class=Expenses_serializer(query,many=True)
        return Response(serializer_class.data)
    def delete(self,request,sid):
        query=Expenses.objects.filter(id=sid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)



