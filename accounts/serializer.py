from rest_framework import serializers

class UserRegisterserializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserProfileUpdateservices(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)