from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AllInfoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'icon',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'description',
        'icon',
        'status',
        'date_add',
        'date_upd',
    )


class HeaderFrontAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'logo',
        'image',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'logo',
        'image',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )


class FooterFrontAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'description',
        'status',
        'date_add',
        'date_upd',
    )


class SocialAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'lien', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'name',
        'lien',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class LocationMapAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'map',
        'laltitude',
        'longitude',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'map',
        'laltitude',
        'longitude',
        'status',
        'date_add',
        'date_upd',
    )


class CopyrightAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )


class InstagramAdmin(admin.ModelAdmin):

    list_display = ('id', 'image', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'image',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.AllInfo, AllInfoAdmin)
_register(models.HeaderFront, HeaderFrontAdmin)
_register(models.FooterFront, FooterFrontAdmin)
_register(models.Social, SocialAdmin)
_register(models.LocationMap, LocationMapAdmin)
_register(models.Copyright, CopyrightAdmin)
_register(models.Instagram, InstagramAdmin)
