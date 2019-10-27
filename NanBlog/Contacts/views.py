from django.shortcuts import render, redirect
from .models import Newsletter, Contact
from rest_framework import viewsets
from .serializer import NewsletterSerializer, ContactSerializer
# from rest_framework_api_key.permissions import HasAPIKey
from django.http import	JsonResponse
import json
from rest_framework import filters
from rest_framework.response import Response
from allConfig.models import *
# Create your views here.

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
class NewsletterViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()
    
class ContactViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


def contact(request):
    return render(request,'pages/contact.html')