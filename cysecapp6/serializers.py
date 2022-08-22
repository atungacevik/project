from rest_framework import serializers
from cysecapp6.models import User6


class User6Serializer(serializers.ModelSerializer):
    class Meta:
        model = User6
        fields = ['name',
                  'username',
                  'credit']

