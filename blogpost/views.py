from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .blog_serializer import blog_serializer

from django.contrib.auth import login as django_login
from rest_framework.authtoken.models import  Token
# Create your views here.

from rest_framework.permissions import IsAuthenticated
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework import permissions

class blog_post(APIView):
    #import pdb;pdb.set_trace()
    permission_classes = [IsAuthenticated]
    authentication_classes = [OAuth2Authentication]
    def post(self,request, format=None):
        serializer = blog_serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


