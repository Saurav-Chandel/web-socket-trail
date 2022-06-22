
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer, CharField


class MessageModelSerializer(serializers.ModelSerializer):
    user = CharField(source='user.username', read_only=True)
    recipient = CharField(source='recipient.username')

    def create(self, validated_data):
        user = self.context['request'].user
        recipient = get_object_or_404(
            User, username=validated_data['recipient']['username'])
        msg = MessageModel(recipient=recipient,
                           body=validated_data['body'],
                           user=user)
        msg.save()
        return msg

    class Meta:
        model = MessageModel
        fields = ('id', 'user', 'recipient', 'timestamp', 'body')


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

