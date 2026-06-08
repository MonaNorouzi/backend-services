from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class CountrySerializer(serializers.Serializer):
    country = serializers.CharField()

class registersealizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ["username", "password"]
    def create (self ,validated_data):
        user = User.objects.create_user(username = validated_data["username"],password = validated_data["password"])
        return user
class editprofserializer(serializers.ModelSerializer):
    
    class Meta :
        model = User
        fields = ["username"]


class loginserializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username,password=password)
        if not user:
            raise serializers.ValidationError("Username or password is incorrect.")

        attrs["user"] = user
        return attrs

   