from django.shortcuts import render
from django.db.models.query_utils import Q

# Create your views here.
import traceback
from turtle import update
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Warehouse_query, transfer_list
from .models import  Transfer, Transfer_detail
from productapp.models import Product
from rest_framework import status
from people.models import Customer
from settingsapp.models import Warehouse, Warehouse_detail
from django.db import transaction
# Create your views here. lyncup
class List_apiview_qrm(APIView):
    def get(self,request,id):
        search = request.GET.get('search')        
        query=Warehouse_detail.objects.filter(Q(product_code__product_code__iexact=search), warehouse=id,active=True)
        serilaizer_class=Warehouse_query(query,many=True)
        return Response(serilaizer_class.data)


class Transfer_api(APIView):
    count=0
    def post(self,request):
        demo=Transfer.objects.all()
        if demo:
            last_entry = Transfer.objects.latest("created_date")
            last_reference_entry=last_entry.id
            a=["%04d" % x for x in range(10000)]
            pid=last_reference_entry+1
            value="TR_{}".format(a[pid])
        else:            
            Transfer_api.count+=1
            a=["%04d" % x for x in range(10000)]
            id=self.count
            value="TR_{}".format(a[id])
        try:
            with transaction.atomic():
                data=request.data
                from_warehouse=Warehouse.objects.get(id=data['tr_from_warehouse'])
                to_warehouse=Warehouse.objects.get(id=data['tr_to_warehouse'])
                reference=data["tr_reference"] if data["tr_reference"] else value
                tr_total_product=len(data['simple_array'])
                tr_update,tr_created=Transfer.objects.update_or_create(
                tr_reference=reference,
                tr_from_warehouse=from_warehouse,
                tr_to_warehouse=to_warehouse,
                tr_total_product=tr_total_product,
                defaults={"tr_date":data['tr_date'], 
                "tr_status":data['tr_status'],
                "tr_additional_discount": data['tr_additional_discount'],
                    "tr_additional_tax": data['tr_additional_tax'],
                    "tr_grand_total":data['tr_grand_total'],
                    "tr_notes":data['tr_notes'],
                    "tr_shipping_charges":data['tr_shipping_charges']})
                for i in data['simple_array']:
                    pr_cd=Product.objects.get(product_code=i["tr_product_code"])
                    product_details_update = Transfer_detail.objects.update_or_create(
                    tr_purchase=tr_update, 
                    tr_product_code=pr_cd,  
                    defaults={"tr_product_cost":i['tr_product_cost'],
                    "tr_product_stock":i['tr_product_stock'],
                    "tr_product_quantity":i['tr_product_quantity'],
                    "tr_product_discount":i['tr_product_discount'],
                    "tr_sub":i['tr_sub'],
                    "tr_product_tax":i['tr_product_tax']                    
                    })                
                if data['tr_status']=='Completed':
                    # for i in data['simple_array']:
                    #     all_stock=Product.objects.filter(product_code=i['tr_product_code']).values('product_stock')
                    #     print(all_stock)
                    #     for j in all_stock:
                           
                    #         total_stock=j["product_stock"]+i['tr_product_quantity']
                           
                    #         demo_update=Product.objects.filter(product_code=i['tr_product_code']).update(product_stock=total_stock) 
                    for i in data['simple_array']:
                        frm_war=Warehouse.objects.get(id=data['tr_from_warehouse'])
                       
                        to_war= Warehouse.objects.get(id=data['tr_to_warehouse'])
                        prd_code=Product.objects.get(product_code=i["tr_product_code"])
                        stock1=Warehouse_detail.objects.filter(warehouse=frm_war,product_code=prd_code).values('stock')
                        stock2=Warehouse_detail.objects.filter(warehouse=to_war,product_code=prd_code).values('stock')
                        print("stock1",stock1)
                        if stock2:
                            for kk in stock1:
                                stock1=kk["stock"]-i["tr_product_quantity"]
                               
                                update1=Warehouse_detail.objects.filter(warehouse=frm_war,product_code=prd_code).update(stock=stock1)
                            for jj in stock2:
                                stock2=jj["stock"]+i["tr_product_quantity"]
                         
                                update2=Warehouse_detail.objects.filter(warehouse=to_war,product_code=prd_code).update(stock=stock2)
                        else:
                            stock=i["tr_product_quantity"]
                            print(stock)
                            war_obj=Warehouse_detail.objects.update_or_create(
                                warehouse=to_war,
                                product_code=prd_code,
                                defaults={
                                "product_cost":i['tr_product_cost'],
                                "stock":stock,
                                "qty":i["tr_product_quantity"],
                                "discount":i['tr_product_discount'],
                                "tax":i["tr_product_tax"],
                                "subtotal":i['tr_sub']})
                            print("st1",stock1)
                            for jk in stock1:
                                print("kk",jk)
                                stock1=jk["stock"]-i["tr_product_quantity"]  
                                update1=Warehouse_detail.objects.filter(warehouse=frm_war,product_code=prd_code).update(stock=stock1)
                return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        query=Transfer.objects.filter(active=True)
        serializer_class=transfer_list(query,many=True)
        return Response(serializer_class.data)
class tr_Particular_api_(APIView):
    def delete(self,request,pid):
        sales_obj=Transfer.objects.filter(id=pid).update(active=False)     
        return Response({"result":"deleted"},status=status.HTTP_200_OK)

#     def get(self,request,sid):
#         query=Sales_return.objects.filter(id=sid)
#         serializer_class=Sr_serializer_header(query,many=True)
#         return Response(serializer_class.data)
# class Sales_return_Payment_api(APIView):
#     def post(self,request,sid):
#         try:
#             payment = Sales_return.objects.get(id=sid)
#             print(payment)
#             with transaction.atomic():
#                 data=request.data   
#                 payment_obj=Sales_return_payment_status.objects.create(
#                 sr_payment_purchase=payment,
#                 sr_payment_date=data['sr_payment_date'],
#                 sr_payment_reference=data['sr_payment_reference'],
#                 sr_payment_choice=data['sr_payment_choice'],
#                 sr_payment_amount=data['sr_payment_amount'],
#                 sr_payment_due=data['sr_payment_due'],
#                 sr_payment_note=data['sr_payment_note'])
#                 sr_sale=Sales_return.objects.filter(id=sid).values('sr_paid')
#                 for i in sr_sale:
#                     paid_amount=i['sr_paid']+data['sr_payment_amount']
#                 edit_method=Sales_return.objects.filter(id=sid).update(sr_paid=paid_amount,sr_due=data['sr_payment_due'],sr_payment_status="Partial")
#                 if data['sr_payment_due']==0:
#                     update=Sales_return.objects.filter(id=sid).update(sr_payment_status="Paid")
#                 return Response({'result':'success'}, status=status.HTTP_200_OK)
#         except Exception:
#             return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
#     def get(self,request,sid):
#         query=Sales_return_payment_status.objects.filter(sr_payment_purchase=sid)
#         serializer_class=Sr_payment_status_serializer(query,many=True)
#         return Response (serializer_class.data)
                

        
