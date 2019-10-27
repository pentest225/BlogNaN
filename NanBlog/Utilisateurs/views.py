from django.shortcuts import render, redirect
from .models import MyUser, Specialite
from django.contrib.auth.models import AbstractUser,Group,Permission
from rest_framework import viewsets
from .serializer import MyUserSerializer, SpecialiteSerializer
# from rest_framework_api_key.permissions import HasAPIKey
from django.http import	JsonResponse
import json
from rest_framework import filters
from rest_framework.response import Response

# Create your views here.

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
class UsersViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()
    
class SpecialiteViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = SpecialiteSerializer
    queryset = Specialite.objects.all()
