from rest_framework import serializers
from cysecapp2.models import User2


class User2Serializer(serializers.ModelSerializer):
    class Meta:
        model = User2
        fields = ('name',
                  'username',
                  'passwd',
                  'course',
                  'auth_token')


class User2AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User2
        fields = ['username', 'auth_token']
