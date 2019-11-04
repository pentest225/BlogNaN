# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'categorie',
        'auteur',
        'titre',
        'afficheImage',
        'affiche',
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
    filter_horizontal = ('tag',)
    search_fields =('titre',)
    def afficheImage(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 50px " />'.format(url=obj.image.url))
    
    def affiche(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 50px " />'.format(url=obj.image_single.url))

class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'article',
        'user',
        'message',
        'sujet',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'status',
        'date_add',
        'date_upd',
    )


class ResponseCommentaireAdmin(admin.ModelAdmin):

    list_display = (
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


class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'article',
        'user',
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
    
class DisLikeAdmin(admin.ModelAdmin):

    list_display = (
        'article',
        'user',
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
_register(models.Like, LikeAdmin)
_register(models.DisLike, DisLikeAdmin)
