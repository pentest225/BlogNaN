from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('email', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
       
    )
    search_fields = ('email',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_display_links = ['email']
    list_per_page = 3
    ordering = ['email']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Newsletter selectionnés"
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les Newsletter selectionnés"

class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'email',
        'message',
        'sujet',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
       
    )
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_display_links = ['nom','email']
    list_per_page = 3
    ordering = ['nom']
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les Messages selectionnés"
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les Messages selectionnés"


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Newsletter, NewsletterAdmin)
_register(models.Contact, ContactAdmin)
