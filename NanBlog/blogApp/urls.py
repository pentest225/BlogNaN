from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CategorieViewset, ArticleViewset, DisLikeViewset, DemandeAdesionViewset, TagViewset, CommentaireViewset, ResponseCommentaireViewset, LikeViewset

router = DefaultRouter()
router.register(r'categorie', CategorieViewset, basename='categorie')
router.register(r'article', ArticleViewset, basename='article')
# router.register(r'archives', ArchiveViewset, basename='archives')
router.register(r'comment', CommentaireViewset, basename='comment')
router.register(r'responsecomment', ResponseCommentaireViewset, basename='responsecomment')
router.register(r'tag', TagViewset, basename='tag')
router.register(r'like', LikeViewset, basename='like')
router.register(r'dislike', DisLikeViewset, basename='dislike')
router.register(r'demande', DemandeAdesionViewset, basename='demande')



from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category/<str:idcat>',views.category,name='category'),
    path('single_blog/<str:idart>',views.single_blog,name='single_blog'),
    path('archive',views.archive,name='archive'),
    path('dashboard',views.dash,name='dash'),
    path('moreInfo/<str:id>',views.moreInfo,name='moreInfo'),
    path('allCat/<str:id>',views.dashCategory,name='dashCategory'),
    path('dashProfil',views.dashProfil,name='dashProfil'),
    path('dashSingleArticle/<str:id>',views.singleArticleDash,name='dashSingleArticle'),
    path('editArticleDash',views.editArticleDash,name='editArticleDash'),
    path('updateArticle',views.updateArticle,name='updateArticle'),
    # path('v_index',views.v_index,name='v_index'),
    # path('v_cat/<int:id>',views.v_cat,name='v_cat'),
    # path('v_single/<int:id>',views.v_single,name='v_single'),
    path('deleteArticle/<int:id>',views.deleteArticle,name='deleteArticle'),
    path('darticle', views.addarticle, name='addarticle'),
    path('saveComment', views.saveComment, name='saveComment'),

    re_path(r'^accounts/', include('allauth.urls')),

    ]
urlpatterns += router.urls

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'
