from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category',views.category,name='category'),
    path('single_blog',views.single_blog,name='single_blog'),
    path('archive',views.archive,name='archive'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('oauth/', include('social_django.urls', namespace='social')),
    ]

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'
