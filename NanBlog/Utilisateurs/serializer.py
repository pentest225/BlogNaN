from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from django.contrib.auth.models import AbstractUser,Group,Permission
from .models import MyUser, Specialite
from allConfig.models import Social

class MyUserSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields= '__all__'
        depth = 1
        
class SpecialiteSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    user_specialiste = MyUserSerializer(many=True, required=False)
    class Meta:
        model = Specialite
        fields= '__all__'
        depth = 1