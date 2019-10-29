# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Specialite, MyUser


@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialiste', 'status', 'date_add', 'date_upd')
    list_filter = ('status', 'date_add', 'date_upd')


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'image',
        'is_staff',
        'is_active',
        'date_joined',
        'description',
        'last_login',
        'is_superuser',
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
    raw_id_fields = ('groups', 'user_permissions', 'specialite', 'social')
