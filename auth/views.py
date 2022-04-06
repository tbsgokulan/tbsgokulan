import traceback
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView

from auth.serializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# from settings.models import UserProfile

class CustomTokenObtainPairView(TokenObtainPairView):

        serializer_class = CustomTokenObtainPairSerializer
