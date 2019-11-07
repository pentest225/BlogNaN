from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views
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
    path('dashboard/categorie/<slug:catname>',views.dcategory,name='dcategory'),
    path('single_blog/<str:idart>',views.single_blog,name='single_blog'),
    path('archive',views.archive,name='archive'),
    # path('moreInfo/<str:id>',views.moreInfo,name='moreInfo'),
    # path('allCat/<str:id>',views.dashCategory,name='dashCategory'),
    # path('updateArticle',views.updateArticle,name='updateArticle'),
    # path('deleteArticle/<int:id>',views.deleteArticle,name='deleteArticle'),
    # path('darticle', views.addarticle, name='addarticle'),
    path('dashboard', views.index_dash, name='index_dash'),
    path('tables_dash/', views.tables_dash, name='tables_dash'),
    path('<int:pk>/project_detail_dash/', views.project_detail_dash, name='project_detail_dash'),
    path('admin_visiteur_dash/', views.admin_visiteur_dash, name='admin_visiteur_dash'),
    path('<int:id>/detail_visiteur_dash', views.detail_visiteur_dash, name='detail_visiteur_dash'),
    path('page_dash/', views.page_dash, name='page_dash'),
    path('post_attend_dash/', views.post_attend_dash, name='post_attend_dash'),
    path('post_partage_dash/', views.post_partage_dash, name='post_partage_dash'),
    path('post_valid_dash/', views.post_valid_dash, name='post_valid_dash'),
    path('form_article_dash/', views.form_article_dash, name='form_article_dash'),
    path('form_profil_dash/', views.form_profil_dash, name='form_profil_dash'),
    path('profil_visiteur_dash/', views.profil_visiteur_dash, name='profil_visiteur_dash'),
    # path('login/', views.connect, name='login'),
    # path('connect/', views.connecter, name='connecter'),
    # path('deconnect/', views.deconection, name='deconnecte'),
    # path('deconnexion/', views.deconection, name='deconnect'),
    path('tables_visiteur_dash/', views.tables_visiteur_dash, name='tables_visiteur_dash'),
    re_path(r'^accounts/', include('allauth.urls')),

    ]
urlpatterns += router.urls

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'
