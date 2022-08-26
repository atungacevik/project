from rest_framework import serializers
from cysecapp10.models import User10


class User10Serializer(serializers.ModelSerializer):
    class Meta:
        model = User10
        fields = ('name',
                  'username',
                  'passwd',
                  'course',
                  'auth_token')