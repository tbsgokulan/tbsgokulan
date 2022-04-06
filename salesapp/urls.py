
from django.urls import path

from salesapp.views import Particular_api_sales, Sales_Payment_api, Sales_api
urlpatterns = [
    path('createsales/',Sales_api.as_view(),name='Sales_api'),
    path('listsales/',Sales_api.as_view(),name='Sales_api'),
    path('deletesales/<pid>/',Particular_api_sales.as_view(),name='Particular_api_sales'),
    # path('edit_sale/<sid>/',Particular_api_sales.as_view(),name='Particular_api_sales'),
    path('list_particular_sale/<sid>/',Particular_api_sales.as_view(),name='Particular_api_sales'),
    path('create_sales_payment/<sid>/',Sales_Payment_api.as_view(),name='Sales_Payment_api'),
    path('list_sales_payment/<sid>/',Sales_Payment_api.as_view(),name='Sales_Payment_api'),
    ]