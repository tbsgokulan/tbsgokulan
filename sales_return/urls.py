from django.urls import path
from .views import Sales_return_Payment_api, Sales_return_api, Sr_Particular_api_sales
urlpatterns = [
    path('create_sale_return/',Sales_return_api.as_view(),name='Sales_return_api'),
    path('list_sale_return/',Sales_return_api.as_view(),name='Sales_return_api'),
    path('delete_sale_return/<pid>/',Sr_Particular_api_sales.as_view(),name='Sr_Particular_api_sales'),
    # path('edit_sale/<sid>/',Particular_api_sales.as_view(),name='Particular_api_sales'),
    path('list_particular_sale_return/<sid>/',Sr_Particular_api_sales.as_view(),name='Sr_Particular_api_sales'),
    path('create_sale_return_payment/<sid>/',Sales_return_Payment_api.as_view(),name='Sales_return_Payment_api'),
    path('list_sale_return_payment/<sid>/',Sales_return_Payment_api.as_view(),name='Sales_return_Payment_api'),
    ]