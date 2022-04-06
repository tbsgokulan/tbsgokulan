import traceback
from turtle import update
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sales_return, Sales_return_detail, Sales_return_payment_status
from .serializers import Sr_payment_status_serializer, Sr_serializer, Sr_serializer_header
from productapp.models import Product
from rest_framework import status
from people.models import Customer
from settingsapp.models import Warehouse, Warehouse_detail
from django.db import transaction
# Create your views here. lyncup

class Sales_return_api(APIView):
    count=0
    def post(self,request):
        demo=Sales_return.objects.all()
        if demo:
            last_entry = Sales_return.objects.latest("created_date")
            last_reference_entry=last_entry.id
            a=["%04d" % x for x in range(10000)]
            pid=last_reference_entry+1
            value="SR_{}".format(a[pid])
        else:            
            Sales_return_api.count+=1
            a=["%04d" % x for x in range(10000)]
            id=self.count
            value="SR_{}".format(a[id])
        try:
            with transaction.atomic():
                data=request.data
                customer=Customer.objects.get(id=data['sr_customer'])
                reference=data["sr_reference"] if data["sr_reference"] else value
                sr_update,sr_created=Sales_return.objects.update_or_create(
                sr_reference=reference,
                sr_date=data['sr_date'],
                sr_customer=customer,
                sr_warehouse=Warehouse.objects.get(id=data['sr_warehouse']),
                defaults={"sr_date":data['sr_date'], 
                "sr_status":data['sr_status'],
                "sr_additional_discount": data['sr_additional_discount'],
                    "sr_additional_tax": data['sr_additional_tax'],
                    "sr_grand_total":data['sr_grand_total'],
                    "sr_notes":data['sr_notes'],
                    "sr_shipping_charges":data['sr_shipping_charges'],
                    "sr_due":data['sr_grand_total']})
                for i in data['simple_array']:
                    product_details_update = Sales_return_detail.objects.update_or_create(
                    sr_purchase=sr_update, 
                    sr_product_code=Product.objects.get(product_code=i["sr_product_code"]),  
                    defaults={"sr_product_cost":i['sr_product_cost'],
                    "sr_product_stock":i['sr_product_stock'],
                    "sr_product_quantity":i['sr_product_quantity'],
                    "sr_product_discount":i['sr_product_discount'],
                    "sr_sub":i['sr_sub'],
                    "sr_product_tax":i['sr_product_tax']
                    })
                if data['sr_status']=='Completed':
                    for i in data['simple_array']:
                        all_stock=Product.objects.filter(product_code=i['sr_product_code']).values('product_stock')
                        print(all_stock)
                        for j in all_stock:
                           
                            total_stock=j["product_stock"]+i['sr_product_quantity']
                           
                            demo_update=Product.objects.filter(product_code=i['sr_product_code']).update(product_stock=total_stock) 
                    for i in data['simple_array']:
                        war=Warehouse.objects.get(id=data['sr_warehouse']) 
                        prd_code=Product.objects.get(product_code=i["sr_product_code"])
                        stock=Warehouse_detail.objects.filter(warehouse=war,product_code=prd_code).values('stock')
                        if stock:
                            for kk in stock:
                                stock=kk["stock"]+i["sr_product_quantity"]
                        else:
                            stock=i["sr_product_quantity"]
                        war_obj=Warehouse_detail.objects.update_or_create(
                            warehouse=war,
                            product_code=prd_code,
                            defaults={
                            "product_cost":i['sr_product_cost'],
                            "stock":stock,
                            "qty":i["sr_product_quantity"],
                            "discount":i['sr_product_discount'],
                            "tax":i["sr_product_tax"],
                            "subtotal":i['sr_sub']}
                        )
                return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        query=Sales_return.objects.filter(active=True)
        serializer_class=Sr_serializer(query,many=True)
        return Response(serializer_class.data)
class Sr_Particular_api_sales(APIView):
    def delete(self,request,pid):
        sales_obj=Sales_return.objects.filter(id=pid).update(active=False)     
        return Response({"result":"deleted"},status=status.HTTP_200_OK)

    def get(self,request,sid):
        query=Sales_return.objects.filter(id=sid)
        serializer_class=Sr_serializer_header(query,many=True)
        return Response(serializer_class.data)
class Sales_return_Payment_api(APIView):
    def post(self,request,sid):
        try:
            payment = Sales_return.objects.get(id=sid)
            print(payment)
            with transaction.atomic():
                data=request.data   
                payment_obj=Sales_return_payment_status.objects.create(
                sr_payment_purchase=payment,
                sr_payment_date=data['sr_payment_date'],
                sr_payment_reference=data['sr_payment_reference'],
                sr_payment_choice=data['sr_payment_choice'],
                sr_payment_amount=data['sr_payment_amount'],
                sr_payment_due=data['sr_payment_due'],
                sr_payment_note=data['sr_payment_note'])
                sr_sale=Sales_return.objects.filter(id=sid).values('sr_paid')
                for i in sr_sale:
                    paid_amount=i['sr_paid']+data['sr_payment_amount']
                edit_method=Sales_return.objects.filter(id=sid).update(sr_paid=paid_amount,sr_due=data['sr_payment_due'],sr_payment_status="Partial")
                if data['sr_payment_due']==0:
                    update=Sales_return.objects.filter(id=sid).update(sr_payment_status="Paid")
                return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
    def get(self,request,sid):
        query=Sales_return_payment_status.objects.filter(sr_payment_purchase=sid)
        serializer_class=Sr_payment_status_serializer(query,many=True)
        return Response (serializer_class.data)
                

        

