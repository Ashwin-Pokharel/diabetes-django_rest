from django.shortcuts import render

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions
from django.contrib.auth import login

# Create your views here.
""""
class LoginView(LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
"""