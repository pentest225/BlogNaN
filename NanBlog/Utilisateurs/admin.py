from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class UtilisateurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'image',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
     
    )
    # raw_id_fields = ('social',)
    filter_horizontal = ('groups','user_permissions','social','specialite')


class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('id', 'specialiste', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
     
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Utilisateur, UtilisateurAdmin)
_register(models.Specialite, SpecialiteAdmin)
