from django.shortcuts import render, redirect
from .models import Categorie, Article, Tag, Commentaire, ResponseCommentaire, Like, DisLike, DemandeAdesion
from rest_framework import viewsets
from .serializer import CategorieSerializer, ArticleSerializer, DisLikeSerializer, DemandeAdesionSerializer, TagSerializer, CommentaireSerializer, ResponseCommentaireSerializer, LikeSerializer
from django.contrib.auth.decorators import login_required
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from django.http import	JsonResponse
import json
from Utilisateurs.models import MyUser
from rest_framework import filters
from rest_framework.response import Response
from .form import ArticleFrom




##################################### import Dashboard groupe 1 ###################################



from django.shortcuts import render, redirect
# from blogger.models import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout






####################################################################################################



# Create your views here.

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
class LikeViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    
class DisLikeViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = DisLikeSerializer
    queryset = DisLike.objects.all()
    
class DemandeAdesionViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = DemandeAdesionSerializer
    queryset = DemandeAdesion.objects.all()
    
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
    
# class ArchiveViewset(viewsets.ModelViewSet):
#     filter_backends = (DynamicSearchFilter,)
#     # permission_classes = [IsAuthenticated|ReadOnly]
#     serializer_class = ArchiveSerializer
#     queryset = Archive.objects.all()
    
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


def category(request, idcat):
    data={
        'idcat':idcat
    }
    return render(request,'pages/category.html',data)

def single_blog(request,idart):
    connect = request.user.username
    print(connect)
    data = {
        'idart':idart,
        'connect':connect
    }
    return render(request,'pages/single_blog.html',data)


def archive(request):
    
    return render(request,'pages/archive.html')



################################################
#               Dashbord root                  #
################################################
# /accounts/logout/
@login_required
def dash(request):
    if request.user.is_authenticated:
        myUser=request.user
        
        allCat=Categorie.objects.filter(status=True)
        allArticle=Article.objects.filter(auteur=request.user,status=True)[:1]
        # j'ai enlever le get car quand il n'y pas d'article il retourne une erreur 
        print("#####################################GROUPE USER  #########################")
        groupeUser=myUser.groups.filter(name='Membre').exists()
        print(groupeUser)
        if groupeUser:
            myForm=ArticleFrom()
            data={
                'allArticle':allArticle,
                'allCat':allCat,
                'myFrom':myForm
            }
            return render(request,'pages/dashM_index.html',data)
        else:
            myForm=ArticleFrom()
            data={
                'allArticle':allArticle,
                'allCat':allCat,
                'myFrom':myForm
            }
            return render(request,'pages/v_index.html',data)
            

def moreInfo(request,id):
    if request.user.is_authenticated:
        myUser=request.user
        allCat=Categorie.objects.filter(status=True)
        allArticle=Article.objects.get(pk=13)
        myForm=ArticleFrom()

        print(allArticle)
        data={
            'allArticle':allArticle,
            'allCat':allCat,
            'myFrom':myForm,
            'id':id
        }
    return render(request,'pages/dashM_moreInfo.html',data)

def dashCategory(request,id):
    allCat=Categorie.objects.filter(status=True)  
    print(allCat)
    myCat=Categorie.objects.get(pk=3)
    allArticle=Article.objects.filter(categorie=myCat,auteur=request.user,status=True)
    data={
        'allArticle':allArticle,
        'cat':myCat,
        'allCat':allCat,
        'idCat':id,
    }
    groupeUser=request.user.groups.filter(name='Membre').exists()
    print(groupeUser)
    if groupeUser:
        return render(request,'pages/dashM_category.html',data)
    else:
        return render(request,'pages/v_cat.html',data)

@login_required
def dashProfil(request):
    
    return render(request,'pages/dashM_profil.html')
    
    
def singleArticleDash(request,id):
    
    data={
        'id':id
    }
    groupeUser=request.user.groups.filter(name='Membre').exists()
    print(groupeUser)
    if groupeUser:
        return render(request,'pages/dashM_single_article.html',data)
    else:
        return render(request,'pages/v_single_article.html',data)

@login_required
def deleteArticle(request,id):
    
    Article.objects.filter(pk=id).delete()
    return redirect('dash')

@login_required
def editArticleDash(request):
    groupeUser=request.user.groups.filter(name='Membre').exists()
    print(groupeUser)
    if groupeUser:
        allCat=Categorie.objects.filter(status=True)
        myFrom=ArticleFrom()
        data={
            'allCat':allCat,
            'myFrom':myFrom
        }
        return render(request,'pages/dashM_edit_article.html',data)
    else:
        return redirect('index')

@login_required
def updateArticle(request):
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = request.POST['name']
    isSuccess=False
    compt=1
    while compt < 10000000:
        compt+=1
    
    action=postdata['action']
    idArcticle=postdata['idArticle']

    if action =="modifStatus":
        myArticle=Article.objects.get(pk=idArcticle)
        myArticle.status= not myArticle.status
        print("++++++++++++++++++")
        print(myArticle)
        myArticle.save()
        print(idArcticle)
        result={
            'updateOk':True
        }
    if action=='addContent':
        comment=postdata['comment']
        idUser=postdata['idUser']
        myArticle=Article.objects.get(pk=idArcticle)
        myU=MyUser.objects.get(pk=idUser)
        newComment=Commentaire(article=myArticle,user=myU,sujet="pas obliger",message=comment)
        newComment.save()
        print("#################################Add comment #######################")
        print(newComment)
        
        result={
            'addCommentOk':True
        }

    return JsonResponse(result, safe=False)

def addarticle(request):
    cat = request.POST.get('cat')
    title = request.POST.get('title')
    description = request.POST.get('email')
    contenu = request.POST.get('contenu')
    user= request.user.id
    
    issucces = False
    
    if cat !='' and title != '' and description != ''  and  contenu != '' :
        image = request.FILES['file']
        issucces = True
        h = Article(categorie=cat,auteur=user,titre=title,description=description, image=image, contenu=contenu)
        h.save()
        print(cat, title, description, contenu)
    else:
        issucces = False
    datas = {
        'succes': issucces,
        'name': title,
    }
    return JsonResponse(datas, safe=False)
################################################
#              PAGE VISITEUR                   #
#                                              #
################################################












############################################# Dashboard groupe 1 ###########################################


@login_required(login_url='login')
def index_dash(request):
    # catego= Article.objects.filter(categorie__pk = pk ).order_by('-id')
    # categorie__id = pk
    # profil= Profile.objects.all()[:1]
    # comment= Commentaire.objects.filter(statut=True, article__valider=True)
    # catego= Category.objects.filter(statut=True)
    # article= Article.objects.filter(statut=True)
    # articl= Article.objects.filter(statut=True, valider=True )
    # articles= Article.objects.filter(statut=True, valider=True )
    # articlee= Article.objects.filter(statut=True, valider=False )
    # context = {"catego": catego, "comment": comment, "profil": profil, "article": article, "articles": articles, "articlee": articlee,}
    
    return render(request, 'pages/index_dash.html')

@login_required(login_url='connecter')
def admin_visiteur_dash(request):
    # article = Article.objects.filter(statut=True, valider=True)
    # commentaires = Commentaire.objects.filter(statut=True, article__valider=True)
    # data = {
    #     'commentaire': commentaires,
    #     'article':article,
    # }
    return render(request, 'pages/admin_visiteur_dash.html')


def connect(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        _next = request.GET.get('next', False)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            
            print("user is login")

            login(request, user)
            if _next: 
                return redirect(_next)
            else:
                return redirect('index_dash')
        else:
            return render(request, 'pages/connexion.html')
    return render(request, 'pages/connexion.html')

def connecter(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        _next = request.GET.get('next', False)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            
            print("user is login")

            login(request, user)
            if _next: 
                return redirect(_next)
            else:
                return redirect('admin_visiteur_dash')
        else:
            return render(request, 'pages/connexion.html')
    return render(request, 'pages/connexion.html')




def deconection(request):
    logout(request)
    return redirect('connect')

def deconexion(request):
    logout(request)
    return redirect('connecter')




def detail_visiteur_dash(request, id):
    # selectarticle = Article.objects.get(pk=id)
    # commentaire = Commentaire.objects.filter(article__id = id, article__valider=True)
    # profil= Profile.objects.all()[:1]
    # context = {
    #     "profil": profil,
    #     'selectarticle':selectarticle,
    #     'commentaire':commentaire,
    #     }
    return render(request, 'pages/detaill_visiteur_dash.html')

def page_dash(request):
    return render(request, 'pages/page_dash.html')

def post_attend_dash(request):
    # profil= Profile.objects.all()[:1]
    # commente= Commentaire.objects.filter(statut=True, article__valider=True)
    # articlee= Article.objects.filter(statut=True, valider=False )
    # context = {"articlee": articlee, "commente": commente, "profil": profil,}
    return render(request, 'pages/post_attend_dash.html')

def post_partage_dash(request):
    # profil= Profile.objects.all()[:1]
    # context = {"profil": profil,"commente": commente,}
    return render(request, 'pages/post_partage_dash.html')

def post_valid_dash(request):
    # profil= Profile.objects.all()[:1]
    # commente= Commentaire.objects.filter(statut=True, article__valider=True)
    # articles= Article.objects.filter(statut=True, valider=True )
    # context = {"articles": articles, "profil": profil,}
    
    return render(request, 'pages/post_valid_dash.html')

def profil_visiteur_dash(request):
    return render(request, 'pages/profil_visiteur_dash.html')

def form_article_dash(request):
    # message = ''
    # catego= Category.objects.filter(statut=True)
    # prof= Profile.objects.all()
    # profil= Profile.objects.all()[:1]
    # commente= Commentaire.objects.filter(statut=True, article__valider=True)
    # context = {"commente": commente, "profil": profil,"prof": prof,"catego": catego}
    
    # if request.method == "POST":
    #     titre = request.POST.get('titre')
    #     user_id = request.POST.get('username')
    #     # user = User.objects.get(pk=5)
    #     categorie_id = request.POST.get('categorie')
    #     categorie = Category.objects.get(pk=2)
    #     image = request.FILES.get('image')
    #     description = request.POST.get('description')
    #     content = request.POST.get('content')
    #     #print("Titre=",titre,"userid=",user_id,"categori_id=",categorie_id,"image=",image,'description=',description,'content=',content)
    #     # print('user=',user)
    #     print('categorie=', categorie)
        
    #     article = Article()
    #     article.titre = titre
    #     # article.user_id = user
    #     article.categorie = categorie
    #     article.image = image
    #     article.description = description
    #     article.valider = False
    #     article.content = content
    #     article.save()
    #     #message="Article enregistré avec succes !"
        
    #     #message="Probleme d'enregistrement!"
    #     #print('error enregistrement')

    # context = {
    #     "commente": commente, 
    #     "profil": profil,
    #     "prof": prof,
    #     "catego": catego,
    #     'message':message,
    # }


    return render(request, 'pages/form_article_dash.html')

def form_profil_dash(request):
    # profil= Profile.objects.all()[:1]
    # commente= Commentaire.objects.filter(statut=True, article__valider=True)
    # context = {"commente": commente,"profil": profil, "profil": profil,}
    return render(request, 'pages/form_profil_dash.html')

def project_detail_dash(request, pk):
    # profil= Profile.objects.all()[:1]
    # commente= Commentaire.objects.filter(statut=True, article__valider=True)
    # article= Article.objects.filter(statut=True)
    # art = Article.objects.get(pk=pk)
    # comment = Commentaire.objects.filter(article__valider = True, article__pk = pk).order_by('-id')
    # context = {"article": article,"profil": profil, "commente": commente, "art": art, "comment": comment,}
    return render(request, 'pages/project_detail_dash.html')

def tables_dash(request):
    # profil= Profile.objects.all()[:1]
    # commente= Commentaire.objects.filter(statut=True, article__valider=True)
    # article= Article.objects.filter(statut=True)
    # context = {"article": article, "commente": commente,"profil": profil,}
    return render(request, 'pages/tables_dash.html')

def tables_visiteur_dash(request):
    # article= Article.objects.filter(statut=True)
    # data = {
    #     'article':article,
    # }
    return render(request, 'pages/tables_visiteur_dash.html')
