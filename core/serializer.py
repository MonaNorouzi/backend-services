from rest_framework import status, serializers
class IranTimeserializer(serializers.Serializer):
    iran_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    
class TargetTimezoneserailizer(serializers.Serializer):
    timezone_name = serializers.CharField(max_length=100)
    target_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)