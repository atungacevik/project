from rest_framework import serializers
from cysecapp3.models import User3, Comment


class User3Serializer(serializers.ModelSerializer):
    class Meta:
        model = User3
        fields = ['name',
                  'username']

class User3ManySerializer(serializers.ModelSerializer):
    class Meta:
        model = User3
        fields = ['name',
                  'username',
                  'latitude',
                  'longitude',
                  'deviceId']


class User3FullSerializer(serializers.ModelSerializer):
    user = User3ManySerializer()
    class Meta:
        model = Comment
        fields = ['user',
                  'comment']
