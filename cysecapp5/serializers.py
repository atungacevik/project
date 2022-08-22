from rest_framework import serializers
from cysecapp5.models import User5


class User5Serializer(serializers.ModelSerializer):
    class Meta:
        model = User5
        fields = ['name',
                  'username']

