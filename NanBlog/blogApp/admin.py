# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
class ArticleInline(admin.TabularInline):
    model = models.Article
    extra = 0

class CategorieAdmin(admin.ModelAdmin):

    list_display = ('nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_display_links = ['nom']
    list_per_page = 5
    ordering = ['nom']
    inlines = [ArticleInline]
        
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer Les Categories selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés Les Categories selectionnés"


class TagAdmin(admin.ModelAdmin):

    list_display = ('nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_per_page = 5
    ordering = ['nom']
    
    # creation des fonction
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Tags selectionnés"
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les Tags selectionnés"


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'categorie',
        'auteur',
        'titre', 
        'vue',
        'status',
        'date_add',
        'date_upd',
        'afficheImage',
        'affiche',
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
    actions = ('active','desactive')
    list_display_links = ['titre','afficheImage','affiche']
    list_per_page = 5
    ordering = ['titre']
    readonly_fields = ['afficheImage','affiche']
    fieldsets = [
        ('Visibité et information',{
            'fields':['titre','auteur','is_archive','status','vue']
        }),
        ('Description et contenue',{
            'fields':['description','contenu']
        }),
        ('tags et  Categorie',{
            'fields':['tag','categorie']
        }),
        ('image  article',{
            'fields':['image','image_single']
        })
    ]
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Articles selectionnés"
    
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les Articles selectionnés"
    def afficheImage(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 50px " />'.format(url=obj.image.url))
    
    def affiche(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 50px " />'.format(url=obj.image_single.url))

class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'article',
        'user',
        'sujet',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'article',
        'status',
        'date_add',
        'date_upd',
    )
    actions = ('active','desactive')
    list_display_links = ['article','user']
    list_per_page = 5
    date_hierarchy = 'date_add'
    # ordering = ['titre']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Commentaires selectionnés"
    
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les Commentaires selectionnés"


class ResponseCommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'user',
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
    actions = ('active','desactive')
    list_display_links = ['user']
    list_per_page = 5
    date_hierarchy = 'date_add'
    # ordering = ['titre']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Commentaires selectionnés"
    
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les Commentaires selectionnés"


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
    actions = ('active','desactive')
    list_display_links = ['article','user']
    list_per_page = 5
    date_hierarchy = 'date_add'
    # ordering = ['titre']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Commentaires selectionnés"
    
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les Commentaires selectionnés"
    
class DisLikeAdmin(admin.ModelAdmin):

    list_display = (
        'article',
        'user',
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
    actions = ('active','desactive')
    list_display_links = ['article','user']
    list_per_page = 5
    date_hierarchy = 'date_add'
    # ordering = ['titre']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Commentaires selectionnés"
    
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été Likes avec succés")
        
    desactive.short_description = "desactivés Les Dislike selectionnés"
    
class DemandeAdesionAdmin(admin.ModelAdmin):

    list_display = (
        'user_id',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user_id',
        'status',
        'date_add',
        'date_upd',
    )
    actions = ('active','desactive')
    list_display_links = ['user_id']
    list_per_page = 5
    date_hierarchy = 'date_add'
    # ordering = ['titre']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Demandes selectionnés"
    
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les Demandes selectionnés"



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.ResponseCommentaire, ResponseCommentaireAdmin)
_register(models.Like, LikeAdmin)
_register(models.DisLike, DisLikeAdmin)
_register(models.DemandeAdesion, DemandeAdesionAdmin)
