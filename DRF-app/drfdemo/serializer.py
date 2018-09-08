from django.contrib.auth.models import User, Group
from rest_framework import serializers


class SimpleObject(object):
    def __init__(self, name):
        self.name = name


class SimpleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)

    def create(self, validated_data):
        return SimpleObject(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance
