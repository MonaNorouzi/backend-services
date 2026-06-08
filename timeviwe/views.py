from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from datetime import datetime
from zoneinfo import ZoneInfo
from countryinfo import CountryInfo
from .serializers import CountrySerializer , registersealizer,loginserializer,editprofserializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny


class IranTimeView(APIView):
    def get(self, request):
        return HttpResponse(datetime.now(ZoneInfo("Asia/Tehran")).strftime("now:%H:%M:%S"))
        
class CountryTimeView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):

        serializer = CountrySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        country = serializer.validated_data["country"]
        return Response(datetime.now(ZoneInfo(country)).strftime("now:%H:%M:%S"))
    

class RegisterView(generics.CreateAPIView):
    serializer_class = registersealizer
    permission_classes = [AllowAny]
    
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post (self, request):
        serializer = loginserializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        return Response( {"refresh" :str(refresh) , "access":str(refresh.access_token)})
    

class EditProfileView(generics.UpdateAPIView):
    serializer_class = editprofserializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
    


        
   