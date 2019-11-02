from django.urls import path
from .views import UsersViewset, SpecialiteViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user', UsersViewset, basename='user')
router.register(r'special', SpecialiteViewset, basename='special')

from . import view

urlpatterns = [
    path('inscription/', view.inscription, name='inscription'),
    path('verification/', view.signup_sendmail, name='sign_send_verif'),
    path('activate/<slug:uidb64>/<slug:token>)/', view.activate, name='activate'),
]
urlpatterns += router.urls