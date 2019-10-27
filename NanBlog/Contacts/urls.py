from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import ContactViewset, NewsletterViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'news', NewsletterViewset, basename='news')
router.register(r'contacts', ContactViewset, basename='contact')

from . import views

urlpatterns = [
    path('contact', views.contact,name='contact'),
    path('message', views.postmessage),
    path('souscription', views.souscription),
]
urlpatterns += router.urls
