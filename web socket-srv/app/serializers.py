
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
    user = CharField(source='user.id')
    recipient = CharField(source='recipient.id')

    def create(self, validated_data):
        user = self.context['request'].user  # user who is online.
        print(user)

        # user = get_object_or_404(
        #     User, id=validated_data['user']['id'])


        print("uuuuuuuuuuuuuuuuuuuuuuuuuu")
        print(user)
        print("uuuuuuuuuuuuuuuuuuuuuuuuuu")

        
        recipient = get_object_or_404(
            User, id=validated_data['recipient']['id'])
        print("rrrrrrrrrrrrrrrrrrrrrrrrr")
        print(recipient) 
        print("rrrrrrrrrrrrrrrrrrrrrrrrr")
        
        msg = MessageModel(recipient=recipient,
                           body=validated_data['body'],
                           user=user)

                        
        msg.save()
        return msg

    class Meta:
        model = MessageModel
        fields = ('id', 'user', 'recipient','timestamp', 'body')
        # fields = ('id', 'user','user_id', 'recipient','recipient_id','timestamp', 'body')


class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username',)

