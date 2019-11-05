from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
       
    )


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'id',
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
        'nom',
       
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Newsletter, NewsletterAdmin)
_register(models.Contact, ContactAdmin)
