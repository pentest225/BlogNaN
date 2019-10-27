from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
      
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'auteur',
        'titre',
        'description',
        'image',
        'contenu',
        'image_single',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'categorie',
        'auteur',
        'status',
        'date_add',
        'date_upd',

    )
    raw_id_fields = ('tag',)


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'article',
        'user',

        'message',
        'sujet',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'article',
        'user',
        'status',
        'date_add',
        'article',
   
    )


class ResponseCommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'comment',
        'user',
        'message',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'comment',
        'user',
        'status',
        'date_add',
        'date_upd',
      
     
    )


class ArchiveAdmin(admin.ModelAdmin):

    list_display = ('id', 'article_id', 'status', 'date_add', 'date_upd')
    list_filter = (
        'article_id',
        'status',
        'date_add',
        'date_upd',
    
    )


class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'article',
        'user',
        'like',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'article',
        'user',
        'status',
        'date_add',
        'date_upd',
  
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.ResponseCommentaire, ResponseCommentaireAdmin)
_register(models.Archive, ArchiveAdmin)
_register(models.Like, LikeAdmin)
