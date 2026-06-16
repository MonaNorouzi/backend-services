from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import get_iran_time, get_timezone_time
from .serializer import IranTimeserializer ,TargetTimezoneserailizer
from rest_framework import status

class IranTimeview(APIView):
    """
    view for getting current Iran time.
    """
    def get(self, request):
        time_data = get_iran_time()
        serializer = IranTimeserializer({"iran_time": time_data})
        return Response(serializer.data, status=status.HTTP_200_OK)

class TargetTimezoneView(APIView):
    """
    view for getting time of a specific timezone (Requires Authentication).
    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = TargetTimezoneserailizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        tz_name = serializer.validated_data['timezone_name']
        time_data = get_timezone_time(timezone_name=tz_name)
        
        out_serializer = TargetTimezoneserailizer({
            "timezone_name": tz_name,
            "target_time": time_data
        })
        
        return Response(out_serializer.data, status=status.HTTP_200_OK)