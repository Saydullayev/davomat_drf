from rest_framework import serializers



class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

class UserInfoSerializer(serializers.Serializer):
    ism = serializers.CharField()
    familiya = serializers.CharField()
    ishdami = serializers.BooleanField()

class Get_DistanceSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    login = serializers.CharField()
    password = serializers.CharField()
