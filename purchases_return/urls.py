from django.urls import path
from .views import Purchases_return_api, purticular_api,Pr_Payment_api
urlpatterns = [
    path('create_purchase_return/', Purchases_return_api.as_view(),name="Purchases_return_api"),
    path('list_purchase_return/', Purchases_return_api.as_view(),name="Purchases_return_api"),
    path('delete_purchase_return/<pid>/', purticular_api.as_view(),name="purticular_api"),
    path('get_purchase_return/<pid>/', purticular_api.as_view(),name="purticular_api"),
    path('create_payment_pr/<sid>/', Pr_Payment_api.as_view(),name="Pr_Payment_api"),
    path('list_payment_pr/<sid>/', Pr_Payment_api.as_view(),name="Pr_Payment_api"),


]