from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include


from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category',views.category,name='category'),
    path('single_blog',views.single_blog,name='single_blog'),
    path('archive',views.archive,name='archive'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    re_path(r'^accounts/', include('allauth.urls')),
    ]

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'
