from rest_framework import serializers
from cysecapp4.models import User4


class User4Serializer(serializers.ModelSerializer):
    class Meta:
        model = User4
        fields = ['name',
                  'username']


class User4AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User4
        fields = ('auth_token',
                  'username')

class User4OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User4
        fields = ['username',
                  'otp']


class User4UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User4
        fields = ['username']


class User4StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User4
        fields = ['username',
                  'state']
