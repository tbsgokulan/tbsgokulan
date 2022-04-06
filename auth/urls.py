# from django.urls import path
# from auth.views import CustomTokenObtainPairView


# urlpatterns = [
#     path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
# ] 



from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]