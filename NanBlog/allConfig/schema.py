import graphene
from graphene import relay , ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *


class AllInfoNode(DjangoObjectType):
    class Meta:
        model = AllInfo
        filter_fields = {
            'titre':['exact','icontains','istartswith'],
            'description':['exact','icontains','istartswith'],
            'icon':['exact','icontains','istartswith'],
        }
        interfaces = (relay.Node,)
class HeaderFrontNode(DjangoObjectType):
    class Meta:
        model = HeaderFront
        filter_fields = {
            'titre':['exact','icontains','istartswith'],
        }
        interfaces = (relay.Node,)
class FooterFrontNode(DjangoObjectType):
    class Meta:
        model = FooterFront
        filter_fields = {
            'titre':['exact','icontains','istartswith'],
            'description':['exact','icontains','istartswith'],
        }
        interfaces = (relay.Node,)
class SocialNode(DjangoObjectType):
    class Meta:
        model = Social
        filter_fields = {
            'name':['exact','icontains','istartswith'],
            'lien':['exact','icontains','istartswith'],
            }
        interfaces = (relay.Node,)
class LocationMapNode(DjangoObjectType):
    class Meta:
        model = LocationMap
        filter_fields = {
            'map':['exact','icontains','istartswith'],
            'latitude':['exact','icontains','istartswith'],
            'longitude':['exact','icontains','istartswith'],
            }
        interfaces = (relay.Node,)
class CopyrightNode(DjangoObjectType):
    class Meta:
        model = Copyright
        filter_fields = {
            'titre':['exact','icontains','istartswith'],
            }
        interfaces = (relay.Node,)
class InstagramNode(DjangoObjectType):
    class Meta:
        model = Instagram
        fields = ('image','status','date_add','date_upd')
        filter_fields = ('status',)
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    
    allinfo = relay.Node.Field(AllInfoNode)
    all_AllInfo = DjangoFilterConnectionField(AllInfoNode)
    headerfront = relay.Node.Field(HeaderFrontNode)
    all_HeaderInfo = DjangoFilterConnectionField(HeaderFrontNode)
    footerfront = relay.Node.Field(FooterFrontNode)
    all_FooterFront = DjangoFilterConnectionField(FooterFrontNode)
    social = relay.Node.Field(SocialNode)
    all_Social = DjangoFilterConnectionField(SocialNode)
    location = relay.Node.Field(LocationMapNode)
    all_location = DjangoFilterConnectionField(LocationMapNode)
    copyright = relay.Node.Field(CopyrightNode)
    all_copyright = DjangoFilterConnectionField(CopyrightNode)
    instagram = relay.Node.Field(InstagramNode)
    all_instagram = DjangoFilterConnectionField(InstagramNode)