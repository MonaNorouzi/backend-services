from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from .selectors import get_iran_time, get_timezone_time
from .services import user_register, user_update

class IranTimeApi(APIView):
    """
    API for getting current Iran time.
    """
    class OutputSerializer(serializers.Serializer):
        iran_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def get(self, request):
        time_data = get_iran_time()
        serializer = self.OutputSerializer({"iran_time": time_data})
        return Response(serializer.data, status=status.HTTP_200_OK)

class TargetTimezoneApi(APIView):
    """
    API for getting time of a specific timezone (Requires Authentication).
    """
    permission_classes = [IsAuthenticated]
    class InputSerializer(serializers.Serializer):
        timezone_name = serializers.CharField(max_length=100)
    class OutputSerializer(serializers.Serializer):
        target_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        time_data = get_timezone_time(timezone_name=serializer.validated_data['timezone_name'])

        out_serializer = self.OutputSerializer({"target_time": time_data})
        return Response(out_serializer.data, status=status.HTTP_200_OK)

class UserRegisterApi(APIView):
    """
    API for user registration.
    """
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=150)
        password = serializers.CharField(write_only=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_register(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

class UserProfileUpdateApi(APIView):
    """
    API for updating user profile (Requires Authentication).
    """
    permission_classes = [IsAuthenticated]
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=150, required=False)
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_update(user=request.user,data=serializer.validated_data)
        return Response({"message": "Profile updated successfully."}, status=status.HTTP_200_OK)