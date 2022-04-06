
import traceback
from turtle import update
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from productapp.models import Product
from rest_framework import status
from people.models import Customer
from salesapp.models import Sales, Sales_detail, Sales_payment_status
from salesapp.serializers import Sales_payment_status_serializer, Sales_serializer, Sales_serializer_detail_edit, Sales_serializer_header
from settingsapp.models import Warehouse, Warehouse_detail
from django.db import transaction
# Create your views here. lyncup

class Sales_api(APIView):
    count=0
    def post(self,request):
        demo=Sales.objects.all()
        print(demo)
        if demo:
            last_entry = Sales.objects.latest("created_date")
            last_reference_entry=last_entry.id
            print(last_reference_entry)
            a=["%04d" % x for x in range(10000)]
            pid=last_reference_entry+1
            value="SL_{}".format(a[pid])
        else:            
            Sales_api.count+=1
            a=["%04d" % x for x in range(10000)]
            id=self.count
            value="SL_{}".format(a[id])
        try:
            with transaction.atomic():
                data=request.data
                customer=Customer.objects.get(id=data['sales_customer'])
                reference=data["sales_reference"] if data["sales_reference"] else value
                sales_update,sales_created=Sales.objects.update_or_create(
                sales_reference=reference,
                sales_date=data['sales_date'],
                sales_customer=customer,
                sales_warehouse=Warehouse.objects.get(id=data['sales_warehouse']),
                # sales_additional_tax=data['sales_additional_tax'],
                # sales_additional_discount=data['sales_additional_discount'],
                # sales_shipping_charges=data['sales_shipping_charges'],
                # sales_grand_total = data['sales_grand_total'],
                # sales_due=data['sales_grand_total'],
                # sales_status=data['sales_status'],
                # sales_notes=data['sales_notes'],
                # sales_reference=reference)
                defaults={"sales_date":data['sales_date'], 
                "sales_status":data['sales_status'],
                "sales_additional_discount": data['sales_additional_discount'],
                    "sales_additional_tax": data['sales_additional_tax'],
                    "sales_grand_total":data['sales_grand_total'],
                    "sales_notes":data['sales_notes'],
                    "sales_shipping_charges":data['sales_shipping_charges'],
                    "sales_due":data['sales_grand_total']})
                for i in data['simple_array']:
                    product_details_update = Sales_detail.objects.update_or_create(
                    sales_purchase=sales_update, 
                    sales_product_code=Product.objects.get(product_code=i["sales_product_code"]),  
                    # sales_product_cost=i['sales_product_cost'],
                    # sales_product_stock=i['sales_product_stock'],
                    # sales_product_quantity=i['sales_product_quantity'],
                    # sales_product_discount=i['sales_product_discount'],
                    # sales_product_tax=i['sales_product_tax'],
                    # sales_sub=i['sales_sub'])
                    defaults={"sales_product_cost":i['sales_product_cost'],
                    "sales_product_stock":i['sales_product_stock'],
                    "sales_product_quantity":i['sales_product_quantity'],
                    "sales_product_discount":i['sales_product_discount'],
                    "sales_sub":i['sales_sub'],
                    "sales_product_tax":i['sales_product_tax']
                    })
                if data['sales_status']=='COMPLETED':
                    for i in data['simple_array']:
                        all_stock=Product.objects.filter(product_code=i['sales_product_code']).values('product_stock')
                        print(all_stock)
                        for j in all_stock:
                           
                            total_stock=j["product_stock"]-i['sales_product_quantity']
                           
                            demo_update=Product.objects.filter(product_code=i['sales_product_code']).update(product_stock=total_stock) 
                    for i in data['simple_array']:
                        war=Warehouse.objects.get(id=data['sales_warehouse']) 
                        prd_code=Product.objects.get(product_code=i["sales_product_code"])
                        stock=Warehouse_detail.objects.filter(warehouse=war,product_code=prd_code).values('stock')
                        if stock:
                            for kk in stock:
                                stock=kk["stock"]-i["sales_product_quantity"]
                        else:
                            stock=i["sales_product_quantity"]
                        war_obj=Warehouse_detail.objects.update_or_create(
                            warehouse=war,
                            product_code=prd_code,
                            defaults={
                            "product_cost":i['sales_product_cost'],
                            "stock":stock,
                            "qty":i["sales_product_quantity"],
                            "discount":i['sales_product_quantity'],
                            "tax":i["sales_product_tax"],
                            "subtotal":i['sales_sub']}
                        )
                return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        query=Sales.objects.filter(active=True)
        serializer_class=Sales_serializer(query,many=True)
        return Response(serializer_class.data)
class Particular_api_sales(APIView):
    def delete(self,request,pid):
        sales_obj=Sales.objects.filter(id=pid).update(active=False)     
        return Response({"result":"deleted"},status=status.HTTP_200_OK)

    def get(self,request,sid):
        query=Sales.objects.filter(id=sid)
        serializer_class=Sales_serializer_header(query,many=True)
        return Response(serializer_class.data)
class Sales_Payment_api(APIView):
    def post(self,request,sid):
        try:
            payment = Sales.objects.get(id=sid)
            print(payment)
            with transaction.atomic():
                data=request.data   
                payment_obj=Sales_payment_status.objects.create(
                sales_payment_purchase=payment,
                sales_payment_date=data['sales_payment_date'],
                sales_payment_reference=data['sales_payment_reference'],
                sales_payment_choice=data['sales_payment_choice'],
                sales_payment_amount=data['sales_payment_amount'],
                sales_payment_due=data['sales_payment_due'],
                sales_payment_note=data['sales_payment_note'])
                sales_sale=Sales.objects.filter(id=sid).values('sales_paid')
                for i in sales_sale:
                    paid_amount=i['sales_paid']+data['sales_payment_amount']
                edit_method=Sales.objects.filter(id=sid).update(sales_paid=paid_amount,sales_due=data['sales_payment_due'],sales_payment_status="PARTIAL")
                if data['sales_payment_due']==0:
                    update=Sales.objects.filter(id=sid).update(sales_payment_status="PAID")
                return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
    def get(self,request,sid):
        query=Sales_payment_status.objects.filter(sales_payment_purchase=sid)
        serializer_class=Sales_payment_status_serializer(query,many=True)
        return Response (serializer_class.data)
                

        
