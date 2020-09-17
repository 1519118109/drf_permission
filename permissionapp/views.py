from django.contrib.auth.models import Permission, Group
from django.shortcuts import render
from rest_framework.authentication import BaseAuthentication, BasicAuthentication
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from permissionapp import models
from permissionapp.authenticator import MyAuth
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.throttling import BaseThrottle, UserRateThrottle
from permissionapp.permission import MyPermission
from permissionapp.thortting import MyRateThrottle


class Demo(APIView):
    # authentication_classes = [BasicAuthentication]

    def get(self, request, *args, **kwargs):
        user = models.User.objects.first()
        print(user.email)
        print(user.groups.first().name)
        print(user.user_permissions.first().name)

        group = Group.objects.first()
        print('----------------------------')
        print(group)
        print(group.user_set.first().username)
        print(group.permissions.first())

        permission = Permission.objects.first()
        print('----------------------------')
        print(permission.name)
        print(permission.user_set.first().username)
        per = Permission.objects.filter(pk=1).first()
        print(per.group_set.first().name)

        return Response("OK")


class UserAPIView(APIView):
    permission_classes = [MyPermission]
    authentication_classes = [MyAuth]
    # throttle_classes = [UserRateThrottle]
    throttle_classes = [MyRateThrottle]
    def get(self, request, *args, **kwargs):
        return Response("读操作")

    def post(self, request, *args, **kwargs):
        return Response("写操作")
