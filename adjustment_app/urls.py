from django.urls import path

from .views import Adjustment_api, get_api
urlpatterns = [
    path('create_adjustment/',Adjustment_api.as_view(),name='Adjustment_api'),
    path('delete_adjustment/<sid>/',Adjustment_api.as_view(),name='Adjustment_api'),
    path('get_particular_adjustment/<sid>/',Adjustment_api.as_view(),name='Adjustment_api'),
    path('get_adjustment/',get_api.as_view(),name='get_api'),



]