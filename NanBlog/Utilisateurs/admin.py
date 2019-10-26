from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MyUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'image',
        'description',
        'specialite',
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
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'image',
        'description',
        'specialite',
        'status',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('groups', 'social')


class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('id', 'specialiste', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'specialiste',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.MyUser, MyUserAdmin)
_register(models.Specialite, SpecialiteAdmin)
