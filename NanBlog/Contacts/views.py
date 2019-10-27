from django.shortcuts import render, redirect
from .models import Newsletter, Contact
from rest_framework import viewsets
from .serializer import NewsletterSerializer, ContactSerializer
from rest_framework_api_key.permissions import HasAPIKey
from django.http import	JsonResponse
import json
from rest_framework import filters
from rest_framework.response import Response
from allConfig.models import *
from django.http import JsonResponse
import json
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
class NewsletterViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()
    
class ContactViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


def contact(request):
    return render(request,'pages/contact.html')

def postform(request):
    nom = request.POST.get('nom')
    sujet = request.POST.get('sujet')
    email = request.POST.get('email')
    message = request.POST.get('message')
    print(nom,sujet,contact,email,message)
    
    issucces = False
    
    # if nom !='' and not nom.isspace() and sujet != '' and not sujet.isspace() and message != '' and not message.isspace() and email != '' and not email.isspace() and phone != '' and not phone.isspace():
    #     issucces = True
    #     h = Contact(nom_complet=nom,sujet=sujet,message=message,email=email)
    #     h.save()
    #     print(nom,sujet,contact,email,message)
    # else:
    #     issucces = False
    datas = {
        'succes': issucces,
        'name': nom,
    }
    return JsonResponse(datas, safe=False)
