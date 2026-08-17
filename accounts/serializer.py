from rest_framework import serializers
from rest_framework import serializers as ModelSerializer
from accounts.models import User

class UserRegisterserializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
    class Meta:
        model = User
        fields = ('username','password')
class UserProfileUpdateservices(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)
