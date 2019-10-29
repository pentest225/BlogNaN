from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CategorieViewset, ArticleViewset, TagViewset, CommentaireViewset, ResponseCommentaireViewset, LikeViewset

router = DefaultRouter()
router.register(r'categorie', CategorieViewset, basename='categorie')
router.register(r'article', ArticleViewset, basename='article')
# router.register(r'archives', ArchiveViewset, basename='archives')
router.register(r'comment', CommentaireViewset, basename='comment')
router.register(r'responsecomment', ResponseCommentaireViewset, basename='responsecomment')
router.register(r'tag', TagViewset, basename='tag')
router.register(r'like', LikeViewset, basename='like')


from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category',views.category,name='category'),
    path('single_blog',views.single_blog,name='single_blog'),
    # path('archive',views.archive,name='archive'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('dashboard',views.dash,name='dash'),
    path('moreInfo/<int:id>',views.moreInfo,name='moreInfo'),
    path('allCatallCat/<int:id>',views.dashCategory,name='dashCategory'),
    path('dashProfil',views.dashProfil,name='dashProfil'),
    path('dashSingleArticle/<int:id>',views.singleArticleDash,name='dashSingleArticle'),
    path('editArticleDash',views.editArticleDash,name='editArticleDash'),
    path('updateArticle',views.updateArticle,name='updateArticle'),
    path('deleteArticle/<int:id>',views.deleteArticle,name='deleteArticle'),
    
    re_path(r'^accounts/', include('allauth.urls')),
    ]
urlpatterns += router.urls

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'
