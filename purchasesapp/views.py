
from encodings import search_function
from itertools import product
import traceback
from turtle import update
from urllib import request
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from people.models import Supplier

from productapp.models import Product
from productapp.serializers import Product_serializer, all_field_product_serializer
from django.db.models.query_utils import Q
from django.db import transaction
from purchasesapp.models import Purchase, payment_status, purchase_detail
from purchasesapp.serializers import Payment_serializers, Purchase_serializer, Purchase_serializer_Header, purchase_detail_serializer
from settingsapp.models import Warehouse, Warehouse_detail
from rest_framework import status
from rest_framework import generics

# Create your views here.
# class Listapiview(ListAPIView):
#     queryset=Product.objects.filter(active=True)
#     serializer_class=Product_serializer    
#     filter_backends=(DjangoFilterBackend,SearchFilter)
#     search_fields=['^product_code','^tax_type','product_name']
class Listapiview(APIView):
    def get(self,request):
        search = request.GET.get('search')        
        query=Product.objects.filter(Q(product_name__icontains=search) | (Q(product_code__icontains=search)), active=True)
        serilaizer_class=all_field_product_serializer(query,many=True)
        return Response(serilaizer_class.data)

class Purchase_api(APIView):
    count=0 
    def post(self,request):
        demo=Purchase.objects.all()
        if demo:
            last_entry = Purchase.objects.latest("created_date")
            last_reference_entry=last_entry.id
            # print(last_reference_entry)
            a=["%04d" % x for x in range(10000)]
            pid=last_reference_entry+1
            value="PR_{}".format(a[pid])
        else:            
            Purchase_api.count+=1   
            a=["%04d" % x for x in range(10000)]
            id=self.count
            value="PR_{}".format(a[id])
    
        try:
            with transaction.atomic():

                data=request.data
                supplier=Supplier.objects.get(id=data['supplier'])
                reference=data["reference"] if data["reference"] else value
                # print(data) 
                purchase_update, purchase_created=Purchase.objects.update_or_create(
                    reference=reference,
                    # additional_discount=data['additional_discount'],
                    # additional_tax=data['additional_tax'],
                    # date=data['date'],
                    # grand_total=data['grand_total'],
                    # notes=data['notes'],
                    # shipping_charges=data['shipping_charges'],                      
                    supplier=Supplier.objects.get(id=data['supplier']),
                    warehouse=Warehouse.objects.get(id=data['warehouse']),
                    # reference=value,
                    # status = data['status'],

                    defaults={"status":data['status'], 
                    "additional_discount": data['additional_discount'],
                    "additional_tax": data['additional_tax'],
                    "date":data['date'],
                    "grand_total":data['grand_total'],
                    "notes":data['notes'],
                    "shipping_charges":data['shipping_charges'],
                    "due":data['grand_total']}
                    )
 

                for i in data['simple_array']:
                    product= Product.objects.get(product_code=i["product_code"])
                    product_details_update = purchase_detail.objects.update_or_create(
                    purchase=purchase_update,    
                    product_code=product,
                    # product_cost=i['product_cost'],
                    # produt_stock=i['produt_stock'],
                    # product_quantity=i['product_quantity'],
                    # product_discount=i['product_discount'],
                    # product_tax=i['product_tax'],
                    # sub=i['sub']                    
                    # )
                    defaults={"product_cost":i['product_cost'],
                    "produt_stock":i['produt_stock'],
                    "product_quantity":i['product_quantity'],
                    "product_discount":i['product_discount'],
                    "sub":i['sub'],
                    "product_tax":i['product_tax']
                    })
                if data['status'] == 'Received':
                    for i in data['simple_array']:
                        all_stock=Product.objects.filter(product_code=i['product_code']).values('product_stock')
                        for j in all_stock:
                            total_stock=j["product_stock"]+i['product_quantity']  
                            demo_update=Product.objects.filter(product_code=i['product_code']).update(product_stock=total_stock)
                    for i in data['simple_array']:
                        war=Warehouse.objects.get(id=data['warehouse']) 
                        prd_code=Product.objects.get(product_code=i["product_code"])
                        stock=Warehouse_detail.objects.filter(warehouse=war,product_code=prd_code).values('stock')
                        if stock:
                            for kk in stock:
                                stock=kk["stock"]+i["product_quantity"]
                        else:
                            stock=i["product_quantity"]
                        war_obj=Warehouse_detail.objects.update_or_create(
                            warehouse=war,
                            product_code=prd_code,
                            defaults={
                            "product_cost":i['product_cost'],
                            "stock":stock,
                            "qty":i["product_quantity"],
                            "discount":i['product_discount'],
                            "tax":i["product_tax"],
                            "subtotal":i['sub']}
                        )
                    
                    #a=["%04d" % x for x in range(10000)]
                    # qurey=Purchase.objects.filter(Purchase__product_code=i['product_code']).values("id")
                    # for j in qurey:
                    #id=1
                    # value="PR_{}".format(a[id])
                    
                    # purchase=Purchase.objects.create(   
                    # purchase=Purchase.objects.filter(Purchase__product_code=i['product_code']).update(
                    # reference=data[value])

                return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
    

class list_purchase(APIView):
    def get(self,request):
        query=Purchase.objects.filter(active=True)
        serializer_class=Purchase_serializer(query,many=True)
        #print(serializer_class.data)
        return Response(serializer_class.data)
class Particular_api(APIView):
    def delete(self,request,pid):
        purchase_obj=Purchase.objects.filter(id=pid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)
    def get(self,request,pid):
        query=Purchase.objects.filter(id=pid)
        serializer_class=Purchase_serializer_Header(query,many=True)
        for i in serializer_class.data:
            print(i)
        return Response(serializer_class.data)
    # def put(self,request,sid):
    #     try:
    #         payment_obj=Purchase.objects.get(id=sid)
    #         serializer_obj=Purchase_serializer(payment_obj,data=request.data,partial=True)
    #         if serializer_obj.is_valid(raise_exception=True):
    #             save_payment=serializer_obj.save()
    #             print(serializer_obj.data["due"])
    #             if serializer_obj.data["due"]==0:
    #                 pur=Purchase.objects.filter(id=sid).values('payment_status')
    #                 for i in pur:
    #                     i["payment_status"]="paid"
    #                     pay_sts=i["payment_status"]
    #                     print(pay_sts)
    #                     demo_pur=Purchase.objects.filter(id=sid).update(payment_status=pay_sts)
    #             return Response({"result":"updated"},status=status.HTTP_200_OK)
    #     except Exception:
    #         return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)

class Payment_api(generics.ListCreateAPIView):
    def post(self,request,sid):
        try:
            payment = Purchase.objects.get(id=sid)
            print(payment)
            with transaction.atomic():
                data=request.data   
                payment_obj=payment_status.objects.create(
                payment_purchase=payment,
                payment_date=data['payment_date'],
                payment_reference=data['payment_reference'],
                payment_choice=data['payment_choice'],
                payment_amount=data['payment_amount'],
                payment_due=data['payment_due'],
                payment_note=data['payment_note'])
                pur1=Purchase.objects.filter(id=sid).values('paid')
                for i in pur1:
                    paid_amt=i['paid']+data['payment_amount']
                edit_method=Purchase.objects.filter(id=sid).update(paid=paid_amt,due=data['payment_due'],payment_status='partial')
                print(edit_method)
                if data["payment_due"]==0:
                    pur=Purchase.objects.filter(id=sid).values('payment_status')
                    for i in pur:
                        i["payment_status"]="paid"
                        pay_sts=i["payment_status"]
                        # print(pay_sts)
                        demo_pur=Purchase.objects.filter(id=sid).update(payment_status=pay_sts)
                return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
    def get(self,request,sid):
        query=payment_status.objects.filter(payment_purchase=sid)
        serializer_class=Payment_serializers(query,many=True)
        return Response(serializer_class.data)