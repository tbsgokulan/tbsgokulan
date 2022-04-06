from django.urls import path

from expensesapp.views import Create_expenses_api, Expenses_category_api
urlpatterns = [
    
    path('create_category/',Expenses_category_api.as_view(),name='Expenses_category_api'),
    path('edit_category/<pid>/',Expenses_category_api.as_view(),name='Expenses_category_api'),
    path('create_expenses/',Create_expenses_api.as_view(),name='Create_expenses_api'),
    path('list_category/',Expenses_category_api.as_view(),name='Expenses_category_api'),
    path('list_expenses/',Create_expenses_api.as_view(),name='Create_expenses_api'),
    path('delete_category/<sid>/',Expenses_category_api.as_view(),name='Expenses_category_api'),
    path('delete_expenses/<sid>/',Create_expenses_api.as_view(),name='Create_expenses_api')
  
]