from rest_framework import serializers
from cysecapp.models import User1


class User1Serializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = ('name',
                  'username',
                  'passwd',
                  'course',
                  'auth_token')