import graphene
from graphene import relay , ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *


class NewletterNode(DjangoObjectType):
    class Meta:
        model = Newsletter
        filter_fields = {
            'email':['exact','icontains','istartswith'],
            'status':['exact','icontains','istartswith'],
        }
        interfaces = (relay.Node,)
class ContactNode(DjangoObjectType):
    class Meta:
        model = Contact
        filter_fields = {
            'nom':['exact','icontains','istartswith'],
            'email':['exact','icontains','istartswith'],
            'message':['exact','icontains','istartswith'],
            'sujet':['exact','icontains','istartswith'],
        }
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    
    newsletter = relay.Node.Field(NewletterNode)
    all_newletter = DjangoFilterConnectionField(NewletterNode)
    contact = relay.Node.Field(ContactNode)
    all_contact = DjangoFilterConnectionField(ContactNode)