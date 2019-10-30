# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin


@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialiste', 'status', 'date_add', 'date_upd')
    list_filter = ('status', 'date_add', 'date_upd')


# @admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'status',
        'date_add',
        'date_upd',
    )
    #raw_id_fields = ('social',)
    # raw_id_fields = ('social',)
    filter_horizontal = ('groups','user_permissions','social','specialite')
    # def afficheImage(self, obj):
    #     return mark_safe('<img src = " {url} " width = " 100px " heigth = " 50px " />'.format(url=obj.image.url))

class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('specialiste', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
     
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.MyUser, MyUserAdmin)
_register(models.Specialite, SpecialiteAdmin)
