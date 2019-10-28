from django.shortcuts import render, redirect
from .models import Categorie, Article, Archive, Tag, Commentaire, ResponseCommentaire, Like
from rest_framework import viewsets
from .serializer import CategorieSerializer, ArticleSerializer, ArchiveSerializer, TagSerializer, CommentaireSerializer, ResponseCommentaireSerializer, LikeSerializer
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from django.http import	JsonResponse
import json
from rest_framework import filters
from rest_framework.response import Response
# Create your views here.

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
class LikeViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    
class ResponseCommentaireViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = ResponseCommentaireSerializer
    queryset = ResponseCommentaire.objects.all()
    
class CommentaireViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = CommentaireSerializer
    queryset = Commentaire.objects.all()
    
class ArchiveViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = ArchiveSerializer
    queryset = Archive.objects.all()
    
class TagViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    
class ArticleViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
class CategorieViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = CategorieSerializer
    queryset = Categorie.objects.all()

def index(request):
    
    return render(request,'pages/index.html')


def category(request):
    
    return render(request,'pages/category.html')

def single_blog(request):
    
    return render(request,'pages/single_blog.html')


def archive(request):
    
    return render(request,'pages/archive.html')

def login(request):
    
    return render(request,'pages/login.html')

def register(request):
    
    return render(request,'pages/register.html')