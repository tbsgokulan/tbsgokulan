from django.urls import path
from . views import detailed_customer, detailed_supplier, list_customer, list_supplier

urlpatterns = [
    
    path('listcustomer/',list_customer.as_view(),name='listcustomer'),
    path('createcustomer/',list_customer.as_view(),name='createcustomer'),
    path('detailedcustomer/<cid>/',detailed_customer.as_view(),name='detailedcustomer'),
    path('editcustomer/<cid>/',detailed_customer.as_view(),name='editcustomer'),
    path('deletecustomer/<cid>/',detailed_customer.as_view(),name='deletecustomer'),
    path('listsupplier/',list_supplier.as_view(),name='listsupplier'),
    path('createsupplier/',list_supplier.as_view(),name='createsupplier'),
    path('detailedsupplier/<sid>/',detailed_supplier.as_view(),name='detailedsupplier'),
    path('editsupplier/<sid>/',detailed_supplier.as_view(),name='editsupplier'),
    path('deletesupplier/<sid>/',detailed_supplier.as_view(),name='deletesupplier'),
    
    
]
  