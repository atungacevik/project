from rest_framework import serializers
from cysecapp7.models import User7


class User7Serializer(serializers.ModelSerializer):
    class Meta:
        model = User7
        fields = ['name',
                  'username',
                  'credit']


class User7CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = User7
        fields = ['sessionCookie']


class User7AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User7
        fields = ['auth_token']
