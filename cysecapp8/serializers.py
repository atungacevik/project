from rest_framework import serializers
from cysecapp8.models import User8


class User8Serializer(serializers.ModelSerializer):
    class Meta:
        model = User8
        fields = ('name',
                  'username',
                  'passwd',
                  'course',
                  'auth_token')


class User8AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User8
        fields = ['username', 'auth_token']
