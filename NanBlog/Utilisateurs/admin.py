from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MyUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'image',
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
