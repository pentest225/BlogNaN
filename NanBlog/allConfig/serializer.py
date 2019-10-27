from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import AllInfo, HeaderFront, FooterFront, Social, LocationMap, Copyright, Instagram
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

class InstagramSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Instagram
        fields= '__all__'
        
class CopyrightSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Copyright
        fields= '__all__'
        
class LocationMapSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = LocationMap
        fields= '__all__'
        
class SocialSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Social
        fields= '__all__'
        
class FooterSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = FooterFront
        fields= '__all__'
        
class HeaderSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = HeaderFront
        fields= '__all__'
        
class InfoSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = AllInfo
        fields= '__all__'