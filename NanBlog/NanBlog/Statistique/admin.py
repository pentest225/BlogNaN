from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ClientAdmin(admin.ModelAdmin):

    list_display = (
        
        'ip',
        'continent',
        'pays',
        'ville',
        'reseau',
        'longitude',
        'latitude',
        'page',
        'date_visite',
    )
    list_filter = (
        'date_visite',
        'ip',
        'continent',
        'pays',
        'ville',
        'reseau',
        'page',
        'date_visite',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Client, ClientAdmin)
