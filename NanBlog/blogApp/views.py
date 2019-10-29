from django.shortcuts import render, redirect
from .models import Categorie, Article, Tag, Commentaire, ResponseCommentaire, Like
from rest_framework import viewsets
from .serializer import CategorieSerializer, ArticleSerializer, TagSerializer, CommentaireSerializer, ResponseCommentaireSerializer, LikeSerializer
# from rest_framework_api_key.permissions import HasAPIKey
from django.http import	JsonResponse
from django.contrib.auth.decorators import login_required
import json
from rest_framework import filters
from rest_framework.response import Response
from Utilisateurs.models import MyUser
from .form import ArticleFrom
# Create your views here.

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
class LikeViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    
class ResponseCommentaireViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = ResponseCommentaireSerializer
    queryset = ResponseCommentaire.objects.all()
    
class CommentaireViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = CommentaireSerializer
    queryset = Commentaire.objects.all()
    
# class ArchiveViewset(viewsets.ModelViewSet):
#     filter_backends = (DynamicSearchFilter,)
#     # permission_classes = [IsAuthenticated|ReadOnly]
#     serializer_class = ArchiveSerializer
#     queryset = Archive.objects.all()
    
class TagViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    
class ArticleViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
class CategorieViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = CategorieSerializer
    queryset = Categorie.objects.all()

def index(request):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INFO USER-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(request.user)
    if request.user.is_authenticated:
        myU=request.user
        print("myU")
        # print(myU.image)
        myUser=MyUser.objects.get(pk=myU.id)
        
        print(myU)
        data={
            'isConnected':True,
            'myUser':myU
        }
    data={
        'isConnected':False
    }
    return render(request,'pages/index.html',data)

def category(request):
    if request.user.is_authenticated:
        myU=request.user
        print(myU.username)
        print(myU.id)
        data={
            'isConnected':True,
            'myUser':myU
        }
    data={
        'isConnected':False
    }
    
    return render(request,'pages/category.html',data)

def single_blog(request):
    if request.user.is_authenticated:
        myU=request.user
        print(myU.username)
        print(myU.id)
        data={
            'isConnected':True,
            'myUser':request.user
        }
    data={
        'isConnected':False
    }
    return render(request,'pages/single_blog.html',data)


def archive(request):
    if request.user.is_authenticated:
        myU=request.user
        print(myU.article_auteur)
        print(myU.id)
        data={
            'isConnected':True,
            'myUser':myU
        }
    data={
        'isConnected':False
    }
    
    return render(request,'pages/archive.html',data)
# def archive(request):
    
#     return render(request,'pages/archive.html')

def login(request):
    
    return render(request,'pages/login.html')

def register(request):
    
    return render(request,'pages/register.html')

################################################
#               Dashbord root                  #
################################################
# /accounts/logout/
@login_required
def dash(request):
    if request.user.is_authenticated:
        myUser=request.user
        allCat=Categorie.objects.filter(status=True)
        print(allCat)
        data={
            'allCat':allCat
        }
        
        
    return render(request,'pages/dashM_index.html',data)

def dashCategory(request,id):
    allCat=Categorie.objects.filter(status=True)  
    print(allCat)
    myCat=Categorie.objects.get(pk=id)
    allArticle=Article.objects.filter(categorie=myCat,auteur=request.user,status=True)
    data={
        'allArticle':allArticle,
        'cat':myCat,
        'allCat':allCat
    }
    print(allArticle)
    return render(request,'pages/dashM_category.html',data)
@login_required
def dashProfil(request):
    
    return render(request,'pages/dashM_profil.html')
    
def singleArticleDash(request,id):
    allCat=Categorie.objects.filter(status=True)
    allArticle=Article.objects.get(pk=id)
    data={
        'allArticle':allArticle,
        'allCat':allCat
    }
    print(allArticle)
    
    return render(request,'pages/dashM_single_article.html',data)

def editArticleDash(request):
    allCat=Categorie.objects.filter(status=True)
    myFrom=ArticleFrom()
    data={
        'allCat':allCat,
        'myFrom':myFrom
    }
    return render(request,'pages/dashM_edit_article.html',data)