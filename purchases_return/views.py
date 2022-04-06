from itertools import product
from django.shortcuts import render
from django.db import transaction
from rest_framework.views import APIView
from purchases_return.serializers import Pr_Payment_serializers, Purchase_return_serializer, Purchase_return_serializer_Header
from people.models import Supplier
from productapp.models import Product
from rest_framework.response import Response
import traceback
from rest_framework import status
from purchases_return.models import Purchases_return, Purchases_return_purchase_detail, payment_status
from settingsapp.models import Warehouse, Warehouse_detail

# Create your views here.
class Purchases_return_api(APIView):
    count=0
    def post(self,request):
        demo=Purchases_return.objects.all()
        if demo:
            last_entry=Purchases_return.objects.latest("created_date")
            last_entry_id=last_entry.id
            a=["%04d" % x for x in range(10000)]
            pid=last_entry_id+1
            value="RT_{}".format(a[pid])
        else:            
            Purchases_return_api.count+=1   
            a=["%04d" % x for x in range(10000)]
            id=self.count
            value="RT_{}".format(a[id])
        try:
            with transaction.atomic():
                data=request.data
                purchases_return_supplierss=Supplier.objects.get(id=data["purchases_return_supplier"])
                purchases_return_warehousess=Warehouse.objects.get(id=data["purchases_return_warehouse"])
                reference=data["purchases_return_reference"] if data["purchases_return_reference"] else value
                purchase_return_update, purchase_return_created=Purchases_return.objects.update_or_create(
                    purchases_return_reference=reference,
                    defaults={
                        "purchases_return_supplier":purchases_return_supplierss,
                        "purchases_return_warehouse":purchases_return_warehousess,
                        "purchases_return_additional_discount":data["purchases_return_additional_discount"],
                        "purchases_return_date":data["purchases_return_date"],
                        "purchases_return_additional_tax":data["purchases_return_additional_tax"],
                        "purchases_return_grand_total":data["purchases_return_grand_total"],
                        "purchases_return_notes":data["purchases_return_notes"],
                        "purchases_return_shipping_charges":data["purchases_return_shipping_charges"],
                        "purchases_return_status":data["purchases_return_status"],
                        "purchases_return_due":data["purchases_return_grand_total"]
                    })
                for i in data["simple_array"]:
                    return_product=Product.objects.get(product_code=i["purchases_return_product_code"])
                    purchases_return_details_update=Purchases_return_purchase_detail.objects.update_or_create(
                    purchases_return_purchase = purchase_return_update,
                    purchases_return_product_code=return_product,
                    defaults={
                    "purchases_return_product_cost":i["purchases_return_product_cost"],
                    "purchases_return_produt_stock":i["purchases_return_produt_stock"],
                    "purchases_return_product_quantity":i["purchases_return_product_quantity"],
                    "purchases_return_product_discount":i["purchases_return_product_discount"],
                    "purchases_return_product_tax":i["purchases_return_product_tax"],
                    "purchases_return_sub":i["purchases_return_sub"]}
                    )
                if data["purchases_return_status"]=="Completed":
                    for i in data['simple_array']:
                        all_stock=Product.objects.filter(product_code=i["purchases_return_product_code"]).values("product_stock")
                        for j in all_stock:
                            total_stock=j["product_stock"]-i['purchases_return_product_quantity']
                            demo_update=Product.objects.filter(product_code=i['purchases_return_product_code']).update(product_stock=total_stock)
                    for i in data['simple_array']:
                        war=Warehouse.objects.get(id=data['purchases_return_warehouse']) 
                        prd_code=Product.objects.get(product_code=i["purchases_return_product_code"])
                        print("prd+code....",prd_code)
                        stock=Warehouse_detail.objects.filter(warehouse=war,product_code=prd_code).values('stock')
                        if stock:
                            for kk in stock:
                                stock=kk["stock"]-i["purchases_return_product_quantity"]
                        else:
                            stock=i["purchases_return_product_quantity"]
                        war_obj=Warehouse_detail.objects.update_or_create(
                            warehouse=war,
                            product_code=prd_code,
                            defaults={
                            "product_cost":i['purchases_return_product_cost'],
                            "stock":stock,
                            "qty":i["purchases_return_product_quantity"],
                            "discount":i['purchases_return_product_discount'],
                            "tax":i["purchases_return_product_tax"],
                            "subtotal":i['purchases_return_sub']}
                        )
                return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        query=Purchases_return.objects.filter(active=True)
        serializer_class=Purchase_return_serializer(query,many=True)
        #print(serializer_class.data)
        return Response(serializer_class.data)
class purticular_api(APIView):
    def delete(self,request,pid):
        purchase_obj=Purchases_return.objects.filter(id=pid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)
    def get(self,request,pid):
        query=Purchases_return.objects.filter(id=pid)
        serializer_class=Purchase_return_serializer_Header(query,many=True)
        return Response(serializer_class.data)
class Pr_Payment_api(APIView):
    def post(self,request,sid):
        try:
            pr_payment = Purchases_return.objects.get(id=sid)
            with transaction.atomic():
                data=request.data   
                pr_payment_obj=payment_status.objects.create(
                pr_payment_purchase=pr_payment,
                pr_payment_date=data['pr_payment_date'],
                pr_payment_reference=data['pr_payment_reference'],
                pr_payment_choice=data['pr_payment_choice'],
                pr_payment_amount=data['pr_payment_amount'],
                pr_payment_due=data['pr_payment_due'],
                pr_payment_note=data['pr_payment_note'])
                pur1=Purchases_return.objects.filter(id=sid).values('purchases_return_paid')
                for i in pur1:
                    paid_amt=i['purchases_return_paid']+data['pr_payment_amount']
                edit_method=Purchases_return.objects.filter(id=sid).update(purchases_return_paid=paid_amt,purchases_return_due=data['pr_payment_due'],purchases_return_payment_status='Partial')
                # print(edit_method)
                if data["pr_payment_due"]==0:
                    pur=Purchases_return.objects.filter(id=sid).update(purchases_return_payment_status="paid")
                    # for i in pur:
                    #     i["payment_status"]="paid"
                    #     pay_sts=i["payment_status"]
                    #     # print(pay_sts)
                    #     demo_pur=Purchase.objects.filter(id=sid).update(payment_status=pay_sts)
                return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)

    def get(self,request,sid):
        query=payment_status.objects.filter(pr_payment_purchase=sid)
        serializer_class=Pr_Payment_serializers(query,many=True)
        return Response(serializer_class.data)
    


