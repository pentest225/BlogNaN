from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import ContactViewset, NewsletterViewset

router = DefaultRouter()
router.register(r'news', NewsletterViewset, basename='news')
router.register(r'contacts', ContactViewset, basename='contact')

from . import views

urlpatterns = [
    path('', views.contact,name='contact')
]
urlpatterns += router.urls
