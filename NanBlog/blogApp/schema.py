import graphene
from graphene import relay, ObjectType , Connection , Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *
from Utilisateurs.models import MyUser
from django_filters import OrderingFilter 
from pprint import pprint
from graphql_relay.node.node import from_global_id
########################################################################################################
#                                                                                                      #
#                               CUSTOM EXTEND USEFULL BASE GRAPHENE CLASS                              #
#                                                                                                      #
########################################################################################################

class ExtendConnection(Connection):
    class Meta:
        abstract = True
    total_count = graphene.Int()
    edge_count = graphene.Int()
    def resolve_total_count(root,info,**kwargs):
        return root.length
    def resolve_edge_count(root,info,**kwargs):
        return len(root.edges)


class CustomNode(relay.Node):
    class Meta:
        name= 'Node'
        
    # @staticmethod
    # def to_global_id(type,id):
    #     print(type,'=============',id,'=================================')
    #     return id
    # @staticmethod
    # def get_node_from_global_id(info,global_id,only_type=None):
    #     model =getattr(Query,info.field_name).field_type._meta.model
    #     print('test1:',model)
    #     print('real test======\r\n',model.objects.get(id=global_id),'\r\n id==',global_id,'\r\n only type :',only_type)
    #     return model.objects.get(id=global_id)
########################################################################################################

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
        connection_class = ExtendConnection
        
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
        order_by = OrderingFilter(
            fields=(
                ('date_add','date_add'),
            )
        )
        interfaces = (relay.Node,)
        connection_class = ExtendConnection
        
class RelayCreateArticle(graphene.relay.ClientIDMutation):
    article = graphene.Field(ArticleNode)
    class Input:
        id = graphene.ID()
        categorie = graphene.ID()
        tag = graphene.String()
        titre = graphene.String()
        description = graphene.String()
        contenu = graphene.String()
        status = graphene.Boolean()
        
    def mutate_and_get_payload(root,info,**kwargs):
        image = info.context.FILES.get('image')
        image_single = info.context.FILES.get('image_single')
        categorie = kwargs.get('categorie') or None
        # auteur = info.context.user or None
        auteur = MyUser.objects.get(pk=1)
        tag = kwargs.get('tag') or None
        titre = kwargs.get('titre') or None
        description = kwargs.get('description') or None
        contenu = kwargs.get('contenu') or None
        status = kwargs.get('status',None)
        id = kwargs.get('id') or None
        
        art = None
        print('=============================================\r\n auteur:',auteur,'\r\ncontext\r\n',info.context,'\r\n=============root============\r\n',root)
        if id :
            id= from_global_id(id)
            id=id[1]
            
        if categorie:
            categorie = from_global_id(categorie)
            categorie=categorie[1]
            categorie = Categorie.objects.get(id=categorie)
        if tag :
            t = tag.split(',')
            tag = []
            for v in t:
                v = from_global_id(v)
                v=v[1]
                utag = Tag.objects.get(pk=v)
                tag.append(utag)
        data = {
            'image':image,
            'image_single':image_single,
            'categorie':categorie,
            'auteur':auteur,
            'titre':titre,
            'description':description,
            'contenu':contenu,
            'status':status,
        }
        if id is None:
            if image and image_single and categorie and auteur and tag and titre and description and contenu :
                print('\r\n tag',tag,'\r\n categorie',categorie)
                
                # art = Article(
                #     image=image,
                #     image_single=image_single,
                #     categorie=categorie,
                #     auteur=auteur,
                #     titre=titre,
                #     description=description,
                #     contenu=contenu,
                #     status=status
                #     )
                
                art = Article(data)
                debug('\r\n',art,'\r\n','test debug')
                art.save()
                for t in tag :
                    pprint(t)
                    art.tag.add(t)
                    art.save()
                    print('ok')
                return RelayCreateArticle(article=art)
            else:
                raise Exception('must be have all data to create article')
        else :
            article =Article.objects.get(id=id)
            field={
                # 'image':lambda v: [article.image := v],
                # 'image_single':lambda v:article.image_single,
                # 'categorie':lambda v:article.categorie,
                # 'tag':lambda v:article.tag,
                # 'titre':lambda v: article.titre = v,
                # 'description':lambda v:article.description,
                # 'contenu':lambda v:article.contenu,
                # 'status':lambda v:article.status
            }
            for k , v in data.items():
                if v :
                    print('key:',k,'=====','value:',v,'id:',id)
                    # field[k](v)
                    art = setattr(article,k,v)
                    # article.titre = data['titre']
                    article.save()
                    print(type(article.titre))
        return RelayCreateArticle(article=art)
        

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
        connection_class = ExtendConnection

class ResponseCommentaireNode(DjangoObjectType):
    class Meta:
        model = ResponseCommentaire
        fields = "__all__"
        filter_fields = {
            'message':['icontains','exact','istartswith'],
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection
class ArchiveNode(DjangoObjectType):
    class Meta:
        model = Archive
        fields = "__all__"
        filter_fields = {
            
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection
        
class LikeNode(DjangoObjectType):
    class Meta:
        model = Archive
        fields = "__all__"
        filter_fields = {
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection
        

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
    relay_create_article = RelayCreateArticle.Field()



####################################################################
########################TEST##################################


def debug(*args):
    for var in args:
        if type(var) is not str:
            pprint(dir(var))
        else :
            print(var)
