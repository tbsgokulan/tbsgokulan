from django.shortcuts import render
from rest_framework.response import Response
import traceback
# Create your views here.
from rest_framework.views import APIView
from django.db import transaction
from adjustment_app.models import Adjustment, Adjustment_detail
from .serializers import Adjustment_serializer
from productapp.models import Product
from settingsapp.models import Warehouse, Warehouse_detail
from rest_framework import status
class Adjustment_api(APIView):
    count=0
    def post(self,request):
        demo=Adjustment.objects.all()
        if demo:
            last_entry = Adjustment.objects.latest("created_date")
            last_reference_entry=last_entry.id
            a=["%04d" % x for x in range(10000)]
            pid=last_reference_entry+1
            value="AD_{}".format(a[pid])
        else:            
            Adjustment_api.count+=1
            a=["%04d" % x for x in range(10000)]
            id=self.count
            value="AD_{}".format(a[id])
        try:
            with transaction.atomic():
                data=request.data
                reference=data["adj_reference"] if data["adj_reference"] else value
                adj_total_product=len(data['simple_array'])
                print("adj_total_product",adj_total_product)
                ad_warehouse=Warehouse.objects.get(id=data['adj_warehouse'])
                adj_update,adj_create=Adjustment.objects.update_or_create(
                adj_reference=reference,
                adj_date=data["adj_date"],
                adj_total_product = adj_total_product,
                defaults={
                    'adj_warehouse':ad_warehouse,
                    'adj_note':data["adj_note"]})
            for i in data["simple_array"]:
                adj_detail=Adjustment_detail.objects.update_or_create(
                adj_header=adj_update,
                adj_product_code=i["adj_product_code"],
                defaults={  
                    "adj_product_name":i["adj_product_name"],
                    "adj_stock":i["adj_stock"],
                    "adj_quantity":i["adj_quantity"],
                    "adj_type":i["adj_type"]})
                # print("len",len(data['simple_array']))
                if i["adj_type"]=="Addition":
                   
                    all_stock=Product.objects.filter(product_code=i['adj_product_code']).values('product_stock')
                    print(all_stock)
                    for j in all_stock:
                        total_stock=j["product_stock"]+i['adj_quantity']
                        demo_update=Product.objects.filter(product_code=i['adj_product_code']).update(product_stock=total_stock) 
                    #warehouse_stock
                    war=Warehouse.objects.get(id=data['adj_warehouse']) 
                    prd_code=Product.objects.get(product_code=i["adj_product_code"])
                    stock=Warehouse_detail.objects.filter(warehouse=war,product_code=prd_code).values('stock')
                    if stock:
                        for kk in stock:
                            stock=kk["stock"]+i["adj_quantity"]
                    else:
                        stock=i["adj_quantity"]
                    war_obj=Warehouse_detail.objects.update_or_create(
                            warehouse=war,
                            product_code=prd_code,
                            defaults={
                            "stock":stock,
                            "qty":i["adj_quantity"]})
                else:
                    all_stock=Product.objects.filter(product_code=i['adj_product_code']).values('product_stock')
                    print(all_stock)
                    for j in all_stock:
                        total_stock=j["product_stock"]-i['adj_quantity']
                        demo_update=Product.objects.filter(product_code=i['adj_product_code']).update(product_stock=total_stock)
                    war=Warehouse.objects.get(id=data['adj_warehouse']) 
                    prd_code=Product.objects.get(product_code=i["adj_product_code"])
                    stock=Warehouse_detail.objects.filter(warehouse=war,product_code=prd_code).values('stock')
                    if stock:
                        for kk in stock:
                            stock=kk["stock"]-i["adj_quantity"]
                    else:
                        stock=i["adj_quantity"]
                    war_obj=Warehouse_detail.objects.update_or_create(
                        warehouse=war,
                        product_code=prd_code,
                        defaults={
                            "stock":stock,
                            "qty":i["adj_quantity"]})
                # total_prd=Adjustment.objects.filter(adj_reference=data["adj_reference"]).update(adj_total_product=len(data['simple_array']))
            return Response({'result':'success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request,sid):
        query=Adjustment.objects.filter(id=sid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)
    def get(self,request,sid):
        query=Adjustment.objects.filter(id=sid)
        serializer_class=Adjustment_serializer(query,many=True)
        return Response (serializer_class.data)
class get_api(APIView):
    def get(self,request):
        query=Adjustment.objects.filter(active=True)
        serializer_class=Adjustment_serializer(query,many=True)
        return Response (serializer_class.data)

