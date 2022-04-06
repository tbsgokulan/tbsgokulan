from django.urls import path
from .views import List_Warehouse, detailed_Brand, detailed_Unit, detailed_Warehouse, list_api_Unit,list_Brand,list_Category,detailed_Category, list_Unit

urlpatterns = [
    
    path('listwarehouse/',List_Warehouse.as_view(),name='listwarehouse'),
    path('particularwarehouse/<pid>/',detailed_Warehouse.as_view(),name='detailedwarehouse'),
    path('createwarehouse/',List_Warehouse.as_view(),name='createwarehouse'),
    path('updatewarehouse/<pid>/',detailed_Warehouse.as_view(),name='updatewarehouse'),
    path('deletewarehouse/<pid>/',detailed_Warehouse.as_view(),name='deletewarehouse'),
    path('listcategory/',list_Category.as_view(),name='listcategory'),
    path('particularcategory/<cid>/',detailed_Category.as_view(),name='detailedcategory'),
    path('createcategory/',list_Category.as_view(),name='createcategory'),
    path('updatecategory/<cid>/',detailed_Category.as_view(),name='updatecategory'),
    path('deletecategory/<cid>/',detailed_Category.as_view(),name='deletecategory'),
    path('listbrand/',list_Brand.as_view(),name='listbrand'),
    path('createbrand/',list_Brand.as_view(),name='createbrand'),
    path('particularbrand/<bid>/',detailed_Brand.as_view(),name='detailedbrand'),
    path('updatebrand/<bid>/',detailed_Brand.as_view(),name='updatebrand'),
    path('deletebrand/<bid>/',detailed_Brand.as_view(),name='deletebrand'),
    path('listunit/',list_Unit.as_view(),name='listunit'),
    path('createunit/',list_Unit.as_view(),name='createunit'),
    path('particularunit/<uid>/',detailed_Unit.as_view(),name='detailedunit'),
    path('updateunit/<uid>/',detailed_Unit.as_view(),name='updateunit'),
    path('deleteunit/<uid>/',detailed_Unit.as_view(),name='deleteunit'),
    path('baseunitapi/',list_api_Unit.as_view(),name='list_api_Unit'),
]
