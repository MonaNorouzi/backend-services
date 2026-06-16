from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import UserRegisterserializer ,UserProfileUpdateservices
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .services import user_register, user_update

class UserRegisterview(APIView):
    """
    API for user registration.
    """
    def post(self, request):
        serializer = UserRegisterserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_register(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

class UserProfileUpdateview(APIView):
    """
    API for updating user profile (Requires Authentication).
    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserProfileUpdateservices(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_update(user=request.user,data=serializer.validated_data)
        return Response({"message": "Profile updated successfully."}, status=status.HTTP_200_OK)
# Create your views here.
