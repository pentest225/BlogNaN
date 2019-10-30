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
        

class RelayCreateTag(graphene.relay.ClientIDMutation):
    tag = graphene.Field(TagNode)
    class Input:
        id = graphene.ID()
        nom = graphene.String()
        status = graphene.Boolean()
    def mutate_and_get_payload(root,info,**kwargs):
        nom = kwargs.get('nom') or None
        status = kwargs.get('status',None)
        id = kwargs.get('id') or None
                    
        tag_modif = None
        if id :
            id= from_global_id(id)
            id=id[1]
        data = {
            'nom':nom,
            'status':status
        }
        if id is None:
            if nom:
                tag_modif = Tag(
                    **data
                )
                print(tag_modif)
                debug(tag_modif)
                tag_modif.save()
                return RelayCreateTag(tag=tag_modif)
            else:
                raise Exception('must be have all data to create Tag')
        else :
            tag_modif = Tag.objects.get(id=id)
            for k , v in data.items():
                print('befor validate\r\n')
                print('key:',k,'=====','value:',v,'id:',id)
                print('\r\n')
                if v or type(v) is bool:
                    print('after validate')
                    print('key:',k,'=====','value:',v,'id:',id)
                    tag_user = setattr(tag_modif,k,v)
                    tag_modif.save()
                    print(getattr(tag_modif,k))
        return RelayCreateTag(tag=tag_modif)

                
    
    
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
        is_archive = graphene.Boolean()
        
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
        is_archive = kwargs.get('is_archive',None) 
        id = kwargs.get('id') or None
        
        art = None
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
            'is_archive':is_archive,
        }
        if id is None:
            if image and image_single and categorie and auteur and tag and titre and description and contenu :
                art = Article(**data)
                art.save()
                for t in tag :
                    art.tag.add(t)
                    art.save()
                return RelayCreateArticle(article=art)
            else:
                raise Exception('must be have all data to create article')
        else :
            article =Article.objects.get(id=id)
            for k , v in data.items():
                if v or type(v) is bool :
                    print('key:',k,'=====','value:',v,'id:',id)
                    if k == 'tag':
                        art = getattr(article,k)
                        for t in v:
                            art.add(t)
                            article.save()
                    else:
                        art = setattr(article,k,v)
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

class RelayCreateComment(graphene.relay.ClientIDMutation):
    comment = graphene.Field(CommentaireNode)
    class Input:
        id = graphene.ID()
        article = graphene.ID()
        nom = graphene.String()
        email = graphene.String()
        message = graphene.String()
        sujet = graphene.String()
        status = graphene.Boolean()
        
    def mutate_and_get_payload(root,info,**kwargs):

        article = kwargs.get('article') or None
        # user = info.context.user or None
        user = MyUser.objects.get(pk=1)
        message = kwargs.get('message') or None
        sujet = kwargs.get('sujet') or None
        status = kwargs.get('status',None)
        id = kwargs.get('id') or None
        
        com = None
        if id :
            id= from_global_id(id)
            id=id[1]
            
        if article:
            article = from_global_id(article)
            article=article[1]
            article = Article.objects.get(id=article)
        data = {
            'article':article,
            'user':user,
            'message':message,
            'sujet':sujet,
            'status':status,
        }
        if id is None:
            if article and message and sujet :
                
                com = Commentaire(
                **data
                )
                
                print(com)
                debug(com)
                com.save()
                
                return RelayCreateComment(comment=com)
            else:
                raise Exception('must be have all data to create comment')
        else :
            commentaire = Commentaire.objects.get(id=id)
            for k , v in data.items():
                if v or type(v) is bool :
                    print('key:',k,'=====','value:',v,'id:',id)
                    com = setattr(commentaire,k,v)
                    commentaire.save()
                    print(getattr(commentaire,k))
        return RelayCreateComment(comment=commentaire)


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

class RelayCreateResponseComment(graphene.relay.ClientIDMutation):
    response = graphene.Field(ResponseCommentaireNode)
    class Input:
        id = graphene.ID()
        commentaire = graphene.ID()
        message = graphene.String()
        status = graphene.Boolean()
            
    def mutate_and_get_payload(root,info,**kwargs):

        commentaire = kwargs.get('commentaire') or None
        # user = info.context.user or None
        user = MyUser.objects.get(pk=1)
        message = kwargs.get('message') or None
        status = kwargs.get('status',None)
        id = kwargs.get('id') or None
            
        com = None
        if id :
            id= from_global_id(id)
            id=id[1]
                
        if commentaire:
            commentaire = from_global_id(commentaire)
            commentaire=commentaire[1]
            commentaire = Commentaire.objects.get(id=commentaire)
        data = {
            'comment':commentaire,
            'user':user,
            'message':message,
            'status':status,
        }
        if id is None:
            if commentaire and message :
                    
                res_com = ResponseCommentaire(
                **data
                )
                    
                print(res_com)
                debug(res_com)
                res_com.save()
                    
                return RelayCreateResponseComment(response=res_com)
            else:
                raise Exception('must be have all data to create comment')
        else :
            commentaire_res = ResponseCommentaire.objects.get(id=id)
            for k , v in data.items():
                print('befor validate\r\n')
                print('key:',k,'=====','value:',v,'id:',id)
                print('\r\n')
                if v or type(v) is bool:
                    print('after validate')
                    print('key:',k,'=====','value:',v,'id:',id)
                    com_res = setattr(commentaire_res,k,v)
                    commentaire_res.save()
                    print(getattr(commentaire_res,k))
        return RelayCreateResponseComment(response=commentaire_res)


class LikeNode(DjangoObjectType):
    class Meta:
        model = Like
        fields = "__all__"
        filter_fields = {
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection
        

class RelayCreateLike(graphene.relay.ClientIDMutation):
    like = graphene.Field(LikeNode)
    class Input:
        id = graphene.ID()
        article = graphene.ID()
        status = graphene.Boolean()
    def mutate_and_get_payload(root,info,**kwargs):
        status = kwargs.get('status',None)
        id = kwargs.get('id') or None
        article = kwargs.get('article') or None
        # user = info.context.user or None
        user = MyUser.objects.get(pk=1)
        like_user=None
        if id :
            id= from_global_id(id)
            id=id[1]
        if article:
            article = from_global_id(article)
            article=article[1]
            article = Article.objects.get(id=article)
        data = {
            'article':article,
            'user':user,
            'status':status,
        }
        if id is None:
            if article :
                        
                like_user = Like(
                **data
                )
                        
                print(like_user)
                debug(like_user)
                like_user.save()
                        
                return RelayCreateLike(like=like_user)
            else:
                raise Exception('must be have all data to create Like')
        else :
            like_user = Like.objects.get(id=id)
            for k , v in data.items():
                if v or type(v) is bool :
                    print('key:',k,'=====','value:',v,'id:',id)
                    like_set = setattr(like_user,k,v)
                    like_user.save()
                    print(getattr(like_user,k))
        return RelayCreateLike(like=like_user)


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

    like = relay.Node.Field(LikeNode)
    all_like = DjangoFilterConnectionField(LikeNode)

class RelayMutation(graphene.AbstractType):
    relay_create_categorie = RelayCreateCategorie.Field()
    relay_create_article = RelayCreateArticle.Field()
    relay_create_comment = RelayCreateComment.Field()
    relay_create_response_comment = RelayCreateResponseComment.Field()
    relay_creat_like = RelayCreateLike.Field()
    relay_create_tag = RelayCreateTag.Field()
####################################################################
########################TEST##################################


def debug(*args):
    for var in args:
        if type(var) is not str:
            pprint(dir(var))
        else :
            print(var)
