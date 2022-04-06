from os import name
from django.urls import path

from settingsapp.views import list_api_Unit, list_Brand, list_Category
from . views import  demounit, detailed_product, list_product, unitfilter

urlpatterns = [
    
    path('listproduct/',list_product.as_view(),name='list_product'),
    path('createproduct/',list_product.as_view(),name='list_product'),
    path('updateproduct/<pid>/',detailed_product.as_view(),name='detailed_product'),
    path('deleteproduct/<pid>/',detailed_product.as_view(),name='detailed_product'),
    path('listcategory/',list_Category.as_view(),name='list_category'),
    path('listbrand/',list_Brand.as_view(),name='list_unit'),
    path('baseunitapi/',list_api_Unit.as_view(),name='list_api_unit'),

    #demounit
    path('demounit/<id>/',demounit.as_view(),name='demounit'),

    path('unitfilter/',unitfilter.as_view(),name='unitfilter'),

]