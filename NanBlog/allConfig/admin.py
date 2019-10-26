# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AllInfoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'phone',
        'ville',
        'commune',
        'email',
        'description',
        'contactText',
        'icon',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
       
        'titre',
        'phone',
        'ville',
        
    )


class workingHoursAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'day',
        'openHours',
        'closeHours',
        'status',
        'date_add',
        'date_upd',
    )
        'day',
        'openHours',
        'closeHours',
        'status',

    )



    list_display = (
        'id',
        'logo',
        'image',
        'index_title',
        'about_title',
        'cat_title',
        'blog_title',
        'contct_title',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
     
    )


class FooterFrontAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'about_text',
        'newslater_text',
        'folow_text',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'titre',
    )


class SocialAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'lien', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'name',
        
    )
    search_fields = ('name',)


class LocationMapAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'map',
        'latitude',
        'longitude',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
       
        'latitude',
        'longitude',
        'status',
       
    )


class CopyrightAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
     
    )


class InstagramAdmin(admin.ModelAdmin):

    list_display = ('id', 'image', 'status', 'date_add', 'date_upd')
    list_filter = (

_register(models.AllInfo, AllInfoAdmin)
_register(models.HeaderFront, HeaderFrontAdmin)
_register(models.FooterFront, FooterFrontAdmin)
_register(models.Social, SocialAdmin)
_register(models.LocationMap, LocationMapAdmin)
_register(models.Copyright, CopyrightAdmin)
_register(models.Instagram, InstagramAdmin)
