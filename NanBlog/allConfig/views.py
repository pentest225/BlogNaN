from django.shortcuts import render, redirect
from .models import *
from rest_framework import viewsets
from .serializer import InfoSerializer, FooterSerializer, HeaderSerializer, SocialSerializer, InstagramSerializer, CopyrightSerializer, LocationMapSerializer
# from rest_framework_api_key.permissions import HasAPIKey
# from rest_framework.permissions import IsAuthenticated
from django.http import	JsonResponse
import json
from rest_framework import filters
from rest_framework.response import Response

# Create your views here.

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
class InfoViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = InfoSerializer
    queryset = AllInfo.objects.all()
    
class FooterViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = FooterSerializer
    queryset = FooterFront.objects.all()
    
class HeaderViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = HeaderSerializer
    queryset = HeaderFront.objects.all()
    
class SocialViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = SocialSerializer
    queryset = Social.objects.all()
    
class InstagramViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = InstagramSerializer
    queryset = Instagram.objects.all()
    
class CopyViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = CopyrightSerializer
    queryset = Copyright.objects.all()
    
class LocationViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = LocationMapSerializer
    queryset = LocationMap.objects.all()