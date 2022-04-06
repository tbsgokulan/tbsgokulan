from re import search
from django.db.models import query
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.shortcuts import render
import traceback
from django.utils import translation
from rest_framework import response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status,serializers
from rest_framework.response import Response
from .models import Brand, Unit, Warehouse,Category
from .serializers import Brand_serializer,Units_serializer, Warehouse_serializer,Category_serializer


# pagination filter and search
# class List_Warehouse(ListAPIView):    
#     queryset=Warehouse.objects.filter(active=True)
#     serializer_class=Warehouse_serializer
#     filter_backends = (DjangoFilterBackend, SearchFilter)
#     search_fields = ['^Warehouse_name','^Warehouse_email' ]
class List_Warehouse(ListAPIView):
    def get(self,request):
        query=Warehouse.objects.filter(active=True)
        serializer_class=Warehouse_serializer(query,many=True)
        return Response(serializer_class.data)
    #post method using keys
    # def post(self,request):

    #     try:      
    #         data=request.data
    #         Warehouse_create=Warehouse.objects.create(
    #         Warehouse_name= data['Warehouse_name'],
    #         Warehouse_phone=data['Warehouse_phone'],
    #         Warehouse_country=data['Warehouse_country'],
    #         Warehouse_city=data['Warehouse_city'],
    #         Warehouse_email=data['Warehouse_email'],
    #         Warehouse_zipcode=data['Warehouse_zipcode'])
    #         return Response({"Result": "Success"}, status=status.HTTP_200_OK)
    #     except Exception:
    #         return Response(traceback.format_exc(), status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            serializer_obj=Warehouse_serializer(data=request.data)
            if serializer_obj.is_valid(raise_exception=True):
                Warehouse_save=serializer_obj.save()
                return Response({"result":"created"},status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)


class detailed_Warehouse(APIView):
    # def get(self,request,pid):
    #     query=Warehouse.objects.filter(id=pid)
    #     serializer_class=Warehouse_serializer(query,many=True)
    #     return Response(serializer_class.data)
    # def post(self,request,id):
    #     data=request.data
    #     update_method=Warehouse.objects.update()
    #def patch(self,request,pid):
        #query=wharehouse.objects.update()   
    def put(self,request,pid):
        try:            
            Warehouse_obj=Warehouse.objects.get(id=pid)            
            serializer_obj=Warehouse_serializer(Warehouse_obj,data=request.data)
            if serializer_obj.is_valid(raise_exception=True):
                Warehouse_save=serializer_obj.save()
                return Response({"result":"updated"},status=status.HTTP_200_OK)
        except Exception:
            return Response(traceback.format_exc(), status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,pid):
        Warehouse_obj=Warehouse.objects.filter(id=pid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)


#create crud for catougery
class list_Category(ListAPIView):
    #pageination
    # queryet=Category.objects.filter(active=True)
    # Serializer_class=Category_serializer
    # filter_backend=(DjangoFilterBackend,SearchFilter)
    # search_fields=[
    #                 '^name',
    #                 '^email',
    #               ]
    def get (self,request):
        query=Category.objects.filter(active=True)
        serializer_class=Category_serializer(query,many=True)
        return Response (serializer_class.data)
    def post(self,request):
        try:
            serializer_obj=Category_serializer(data=request.data)
            if serializer_obj.is_valid(raise_exception=True):
                Category_save=serializer_obj.save()
                return Response({"result":"created"},status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
class detailed_Category(APIView):
    # def get(self,request,cid):
    #     query=Category.objects.filter(id=cid)
    #     serializer_class=Category_serializer(query,many=True)
    #     return Response(serializer_class.data)
    def put(self,request,cid):
        try:
            Category_obj=Category.objects.get(id=cid)
            serializer_obj=Category_serializer(Category_obj,data=request.data)
            if serializer_obj.is_valid(raise_exception=True):
                Category_save=serializer_obj.save()
                return Response({"result":"updated"},status=status.HTTP_200_OK)
        except Exception:
            return Response (serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,cid):
        Category_obj=Category.objects.filter(id=cid).update(active=False)
        return Response({"sucess":"deleted"},status=status.HTTP_200_OK)
#crud in Brand
class list_Brand(APIView):
    def get(self,request):
        
        query=Brand.objects.filter(active=True)
        serializers_class=Brand_serializer(query,many=True)
        return Response(serializers_class.data)
     
    def post(self,request):

        try:
            data=request.data
            brand=Brand.objects.create(
            brand_name=data['brand_name'],
            brand_description=data['brand_description'],
            brand_image=data['brand_image'])
            return Response({"result":"created"},status=status.HTTP_200_OK)

        except Exception:
            return Response(traceback.format_exc(), status=status.HTTP_400_BAD_REQUEST)

class detailed_Brand(APIView):
    # def get(self,request,bid):
    #     query=Brand.objects.filter(id=bid)
    #     Serializer_class=Brand_serializer(query,many=True)
        # return Response (Serializer_class.data)
    def put(self,request,bid):
        try:
            Brand_obj=Brand.objects.get(id=bid)
            serializer_obj=Brand_serializer(Brand_obj,data=request.data)
            if serializer_obj.is_valid(raise_exception=True):
                Brand_save=serializer_obj.save()
                return Response({"result":"updated"},status=status.HTTP_200_OK)
        except Exception:
            return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,bid):
        Brand_obj=Brand.objects.filter(id=bid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)

#crud for Unit
class list_api_Unit(APIView):
    def get(self,request):
        query=Unit.objects.filter(base_unit="",active=True)
        serializer_class=Units_serializer(query,many=True)
        return Response(serializer_class.data)

class list_Unit(APIView):
    # def get(self,request):
    #     query=Unit.objects.all()
    #     serializer_class=Unit_serializer(query,many=True)
    #     return Response(serializer_class.data)
    def get(self,request):
        query=Unit.objects.filter(active=True)
        serializer_class=Units_serializer(query,many=True)
        return Response(serializer_class.data)
    
    def post(self,request):
        try:
            data=request.data
            Unit_obj=Unit.objects.create(
            unit_name=data['unit_name'],
            short_name=data['short_name'],
            base_unit=data['base_unit'],
            operator=data['operator'],
            operation_value=data['operation_value'])
            return Response({"sucess":"created"},status=status.HTTP_200_OK)

        except Exception:
            return Response(traceback.format_exc(), status=status.HTTP_400_BAD_REQUEST)

class detailed_Unit(APIView):
    # def get(self,request,uid):
    #     query=Unit.objects.filter(id=uid)
    #     serializer_class=Unit_serializer(query,many=True)
    #     return Response(serializer_class.data)
    def put(self,request,uid):
        try:
            Unit_obj=Unit.objects.get(id=uid)
            serializer_obj=Units_serializer(Unit_obj,data=request.data)
            if serializer_obj.is_valid(raise_exception=True):
                save_Unit=serializer_obj.save()
                return Response({"result ":"updated"},status=status.HTTP_200_OK)
        except Exception:
            return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,uid):
        Unit_obj=Unit.objects.filter(id=uid).update(active=False)
        return Response({"result":"deleted"},status=status.HTTP_200_OK)

