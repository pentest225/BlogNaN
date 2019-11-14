from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MyUserAdmin(admin.ModelAdmin):

    list_display = (
        'afficheImage',
        'username',
        'first_name',
        'last_name',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
     
    )
    search_fields = ('username',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_display_links = ['username','first_name']
    list_per_page = 5
    ordering = ['first_name']
    readonly_fields = ['afficheImage']
    filter_horizontal = ('groups','user_permissions','social','specialite')
    fieldsets = [
        ('Identification utilisateur',{
            'fields':['username','first_name','last_name','image','specialite','social']
        }),
        ('Groupe et Visibilité',{
            'fields':['status','groups']
        }),
    ]
    
    def afficheImage(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 50px " />'.format(url=obj.image.url))
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Utilisateurs selectionnés"
    
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les sousCategorie selectionnés"

class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('specialiste', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
     
    )
    search_fields = ('specialiste',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_display_links = ['specialiste']
    list_per_page = 3
    ordering = ['specialiste']
    
    # creation des fonction
    
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Specialité selectionnés"
    
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les Utilisateurs  selectionnés"
    


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.MyUser, MyUserAdmin)
_register(models.Specialite, SpecialiteAdmin)
