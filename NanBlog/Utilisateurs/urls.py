from django.urls import path
from .views import UsersViewset, SpecialiteViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user', UsersViewset, basename='user')
router.register(r'special', SpecialiteViewset, basename='special')

from . import views

urlpatterns = [
]
urlpatterns += router.urls