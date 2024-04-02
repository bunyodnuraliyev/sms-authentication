from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers
    permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]