from django.urls import path

from .views import List_apiview_qrm, Transfer_api,tr_Particular_api_
urlpatterns = [
    
    path('transfer_id/<id>/',List_apiview_qrm.as_view(),name='List_apiview_qrm'),
    path('create_transfer/',Transfer_api.as_view(),name='Transfer_api'),
    path('list_transfer/',Transfer_api.as_view(),name='Transfer_api'),
    path('delete_transfer/<pid>/',tr_Particular_api_.as_view(),name='tr_Particular_api_'),




    ]