import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *


# class CustomNode(relay.Node):
#     class Meta:
#         name='Node'
        
#     # @staticmethod
#     # def to_global_id(type,id):
#     #     return id
    

class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        fields = "__all__"
        filter_fields = {
            'nom':['exact','icontains','istartswith'],
        }
        interfaces = (relay.Node,)
        

class CategorieNode(DjangoObjectType):
    class Meta:
        model = Categorie
        fields = "__all__"
        filter_fields = {
            'nom':['exact','icontains'],
        }
        interfaces = (relay.Node,)
        
class RelayCreateCategorie(graphene.relay.ClientIDMutation):
    categorie = graphene.Field(CategorieNode)
    class Input:
        nom = graphene.String()
        status = graphene.Boolean()
        pk = graphene.ID()
    def mutate_and_get_payload(root,info,**kwargs):
        pk = kwargs.get('id') or None
        nom = kwargs.get('nom') or None
        status = kwargs.get('status') or None
        if nom is not None and status is not None and pk is None:
            cat = Categorie(nom=nom,status=status)
        elif nom is not None and status is not None and pk is not None :
            cat = Categorie.objects.get(pk=pk)
            cat.nom=nom
            cat.status = status
        elif nom is not None and status is None and pk is not None:
            cat = Categorie.objects.get(pk=pk)
            cat.nom=nom
        elif nom is None and status is not None and pk is not None:
            cat = Categorie.objects.get(pk=pk)
            cat.status=status
        else:
            raise Exception('must be give parameters for Categorie mutations')
        cat.save()
        return RelayCreateCategorie(categorie=cat)
    
class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        fields = "__all__"
        filter_fields = {
            'titre':['icontains','exact','istartswith'],
            'description':['icontains','exact','istartswith'],
            'contenu':['icontains','exact','istartswith'],
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        
# class RelayCreateArticle(DjangoObjectType):
#     article = graphene.Field(ArticleNode)
#     class Input:
#         categorie = graphene.ID()
#         auteur = graphene.ID()
#         tag = graphene.Scalar()
#         titre = graphene.String()
#         description = graphene.String()
#         contenu = graphene.String()
#         status = graphene.Boolean()
        
#     def mutate_and_get_payload(root,info,**kwargs):
#         image = info.context.FILES.get('image')
#         image_single = info.context.FILES.get('image_single')
        

    
class CommentaireNode(DjangoObjectType):
    class Meta:
        model = Commentaire
        fields = "__all__"
        filter_fields = {
            'message':['icontains','exact','istartswith'],
            'sujet':['icontains','exact','istartswith'],
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        
class ResponseCommentaireNode(DjangoObjectType):
    class Meta:
        model = ResponseCommentaire
        fields = "__all__"
        filter_fields = {
            'message':['icontains','exact','istartswith'],
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        
class ArchiveNode(DjangoObjectType):
    class Meta:
        model = Archive
        fields = "__all__"
        filter_fields = {
            
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        
class LikeNode(DjangoObjectType):
    class Meta:
        model = Archive
        fields = "__all__"
        filter_fields = {
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        

class Query(graphene.ObjectType):
    article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)
    
    category = relay.Node.Field(CategorieNode)
    all_categories = DjangoFilterConnectionField(CategorieNode)
    
    tag = relay.Node.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TagNode)
    
    comment = relay.Node.Field(CommentaireNode)
    all_comments = DjangoFilterConnectionField(CommentaireNode)
    
    response = relay.Node.Field(ResponseCommentaireNode)
    all_response = DjangoFilterConnectionField(ResponseCommentaireNode)

    archive = relay.Node.Field(ArchiveNode)
    all_archive = DjangoFilterConnectionField(ArchiveNode)
    
    like = relay.Node.Field(LikeNode)
    all_like = DjangoFilterConnectionField(LikeNode)

class RelayMutation(graphene.AbstractType):
    relay_create_categorie = RelayCreateCategorie.Field()
    
