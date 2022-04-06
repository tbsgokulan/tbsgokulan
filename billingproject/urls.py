"""billingproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('settingsapp/',include('settingsapp.urls')),
    path('auth/',include('auth.urls')),
    path('people/',include('people.urls')),
    path('productapp/',include('productapp.urls')),
    path('purchasesapp/',include('purchasesapp.urls')),
    path('sales/',include('salesapp.urls')),
    path('expenses/',include('expensesapp.urls')),
    path('purchases_return/',include('purchases_return.urls')),
    path('sales_return/',include('sales_return.urls')),
    path('adjustment_app/',include('adjustment_app.urls')),
    path('transfer_app/',include('transfer_app.urls'))


]
