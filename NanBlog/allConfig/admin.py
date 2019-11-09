# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class AllInfoAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'phone',
        'ville',
        'commune',
        'email',
        'contactText',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre','ville']
    list_per_page = 10
    actions = ('active','desactive')
    ordering = ['titre']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer Les configuration selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés Les configuration selectionnés"


# class workingHoursAdmin(admin.ModelAdmin):

#     list_display = (
#         'id',
#         'day',
#         'openHours',
#         'closeHours',
#         'status',
#         'date_add',
#         'date_upd',
#     )
#     list_filter = (
#         'status',
#         'date_add',
#         'date_upd',
#         'id',
#         'day',
#         'openHours',
#         'closeHours',
#         'status',
#         'date_add',
#         'date_upd',
#     )


class HeaderFrontAdmin(admin.ModelAdmin):

    list_display = (
        'affiche_logo',
        'titre',
        'index_title',
        'about_title',
        'cat_title',
        'blog_title',
        'contct_title',
        'status',
        'date_add',
        'date_upd',
        'affiche_image',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre','affiche_logo','affiche_image']
    list_per_page = 10
    actions = ('active','desactive')
    ordering = ['titre']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer Les configuration selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés Les configuration selectionnés" 
       
    def affiche_image(self,obj):
        return mark_safe('<img src = "{url}" width = " 100px " heigth = " 100px " />'.format(url=obj.image.url))
    
    def affiche_logo(self,obj):
        return mark_safe('<img src = "{url}" width = " 100px " heigth = " 100px " />'.format(url=obj.logo.url))
    


class FooterFrontAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'about_text',
        'newslater_text',
        'folow_text',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    list_per_page = 10
    actions = ('active','desactive')
    ordering = ['titre']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer Les configuration selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés Les configuration selectionnés"

class SocialAdmin(admin.ModelAdmin):

    list_display = ('name', 'lien', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)
    date_hierarchy = 'date_add'
    list_display_links = ['name']
    list_per_page = 10
    actions = ('active','desactive')
    ordering = ['name']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer Les configuration selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés Les configuration selectionnés"


class LocationMapAdmin(admin.ModelAdmin):

    list_display = (
        'map',
        'latitude',
        'longitude',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    date_hierarchy = 'date_add'
    list_display_links = ['map']
    list_per_page = 10
    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer Les configuration selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés Les configuration selectionnés"
    

class CopyrightAdmin(admin.ModelAdmin):

    list_display = ('titre', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    list_per_page = 10
    actions = ('active','desactive')
    ordering = ['titre']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer Les configuration selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés Les configuration selectionnés"

class InstagramAdmin(admin.ModelAdmin):

    list_display = ('affiche_image', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    # search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['affiche_image']
    list_per_page = 10
    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer Les configuration selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés Les configuration selectionnés"
    def affiche_image(self,obj):
        return mark_safe('<img src = "{url}" width = " 100px " heigth = " 100px " />'.format(url=obj.image.url)) 




def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.AllInfo, AllInfoAdmin)
# _register(models.workingHours, workingHoursAdmin)
_register(models.HeaderFront, HeaderFrontAdmin)
_register(models.FooterFront, FooterFrontAdmin)
_register(models.Social, SocialAdmin)
_register(models.LocationMap, LocationMapAdmin)
_register(models.Copyright, CopyrightAdmin)
_register(models.Instagram, InstagramAdmin)


