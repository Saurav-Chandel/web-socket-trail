# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication

from main import settings
from .serializers import MessageModelSerializer, ProfileModelSerializer
from .models import MessageModel,Profile


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    SessionAuthentication scheme used by DRF. DRF's SessionAuthentication uses
    Django's session framework for authentication which requires CSRF to be
    checked. In this case we are going to disable CSRF tokens for the API.
    """

    def enforce_csrf(self, request):
        return


class MessagePagination(PageNumberPagination):
    """
    Limit message prefetch to one page.
    """
    page_size = settings.MESSAGES_TO_LOAD




def index(request,group_name):
    print("group Name...",group_name)
    groupname=group_name
    # group=Group.objects.filter(name=group_name).first()  #checks the group is already exists.
    # print("Group...",group)
    # chats=[] 
    # if group:
    #     chats=Chat.objects.filter(group=group)
    #     print("chats....",chats)

    # else:
    #     group=Group(name=group_name)
    #     group.save()
    return render(request, 'app/index.html',{'groupname':group_name})


class MessageModelViewSet(ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelSerializer
    allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS','DELETE')
    # authentication_classes = (CsrfExemptSessionAuthentication,)
    pagination_class = MessagePagination      #  this is used for pagination.

    def list(self, request, *args, **kwargs):

        # print(groupname)
        # print(request)
        # print("list")
        self.queryset = self.queryset.filter(Q(recipient=request.user) |
                                             Q(user=request.user))   
                                                             
        target = self.request.query_params.get('target', None)
        print(target)
        if target is not None:
            self.queryset = self.queryset.filter(
                Q(recipient=request.user, user=target) |
                Q(recipient__username=target, user=request.user))
        return super(MessageModelViewSet, self).list(request, *args, **kwargs)


    def retrieve(self, request, *args, **kwargs):
        print("retrieve")
        msg = get_object_or_404(
            self.queryset.filter(Q(recipient=request.user) |
                                 Q(user=request.user),
                                 Q(pk=kwargs['pk'])))
        serializer = self.get_serializer(msg)
        return Response(serializer.data)


class ProfileModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileModelSerializer
    allowed_methods = ('GET', 'HEAD', 'OPTIONS')
    pagination_class = None  # Get all user

    def list(self, request, *args, **kwargs):
        # Get all users except yourself
        self.queryset = self.queryset.exclude(id=request.user.id)
        return super(ProfileModelViewSet, self).list(request, *args, **kwargs)








