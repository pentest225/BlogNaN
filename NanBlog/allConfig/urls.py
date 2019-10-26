from django.urls import path
from .views import InfoViewset, FooterViewset, HeaderViewset, SocialViewset, CopyViewset, LocationViewset, InstagramViewset

router = DefaultRouter()
router.register(r'info', InfoViewset, basename='info')
router.register(r'foot', FooterViewset, basename='foot')
router.register(r'head', HeaderViewset, basename='head')
router.register(r'social', SocialViewset, basename='social')
router.register(r'copy', CopyViewset, basename='copy')
router.register(r'location', LocationViewset, basename='location')
router.register(r'instagram', InstagramViewset, basename='instagram')

urlpatterns = [
]
urlpatterns += router.urls