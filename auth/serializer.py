from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from settings.models import UserProfile
from rest_framework.response import Response
from rest_framework import status
import traceback

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):

        try:
            data = super().validate(attrs)
            refresh = self.get_token(self.user)
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            return data
        except Exception:
            return Response(traceback.format_exc(), status=status.HTTP_400_BAD_REQUEST)
