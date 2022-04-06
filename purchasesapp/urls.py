from os import name
from django.urls import path

from purchasesapp.views import Listapiview, Particular_api, Payment_api, Purchase_api, list_purchase
urlpatterns = [
    
    path('listproductcode/',Listapiview.as_view(),name='Listapiview'),
    path('purchase_product/',Purchase_api.as_view(),name='Purchase_api'),
    # path('purchase_product/<id>/',Purchase_api.as_view(),name='Purchase_api'),

    path('listpurchase/',list_purchase.as_view(),name='list_purchase'),
    path('delete_purchase/<pid>/',Particular_api.as_view(),name='Particular_api'),
    path('update_purchase/<pid>/',Particular_api.as_view(),name='Particular_api'),
    path('update2_purchase/<sid>/',Payment_api.as_view(),name='Payment_api'),
    path('list_payment/<sid>/',Payment_api.as_view(),name='Payment_api'),
   
   
    ]