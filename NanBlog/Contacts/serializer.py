from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import Newsletter, Contact
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

class NewsletterSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields= '__all__'
        
class ContactSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields= '__all__'