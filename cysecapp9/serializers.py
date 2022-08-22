from rest_framework import serializers
from cysecapp9.models import User9


class User9Serializer(serializers.ModelSerializer):
    class Meta:
        model = User9
        fields = ('name',
                  'username',
                  'passwd',
                  'course',
                  'auth_token')


class User9AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User9
        fields = ['username', 'auth_token']
