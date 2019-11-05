import graphene
from graphene import relay , ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *


class ClientNode(DjangoObjectType):
    class Meta:
        model = Client
        filter_fields = {
            'ip':['exact','icontains','istartswith'],
            'continent':['exact','icontains','istartswith'],
            'pays':['exact','icontains','istartswith'],
            'ville':['exact','icontains','istartswith'],
            'reseau':['exact','icontains','istartswith'],
            'longitude':['exact','icontains','istartswith'],
            'latitude':['exact','icontains','istartswith'],
            'page':['exact','icontains','istartswith'],
        }
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    
    client = relay.Node.Field(ClientNode)
    all_client = DjangoFilterConnectionField(ClientNode)