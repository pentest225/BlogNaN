import graphene
from graphene import relay , ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *


class MyUserNode(DjangoObjectType):
    class Meta:
        model = MyUser
        filter_fields = {
            'username':['exact','icontains','istartswith'],
            'first_name':['exact','icontains','istartswith'],
            'last_name':['exact','icontains','istartswith'],
            'email':['exact','icontains','istartswith'],
            'description':['exact','icontains','istartswith'],
            'groups':['exact','icontains','istartswith'],
            'status':['exact','icontains','istartswith'],
        }
        interfaces = (relay.Node,)

class SpecialiteNode(DjangoObjectType):
    class Meta:
        model = Specialite
        filter_fields = {
            'specialiste':['exact','icontains','istartswith'],
            'status':['exact','icontains','istartswith'],
        }
        interfaces = (relay.Node,)
        
class Query(graphene.ObjectType):
    user = relay.Node.Field(MyUserNode)
    all_user = DjangoFilterConnectionField(MyUserNode)
    specialite = relay.Node.Field(SpecialiteNode)
    all_specialite = DjangoFilterConnectionField(SpecialiteNode)