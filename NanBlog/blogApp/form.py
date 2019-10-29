from django import forms
from .models import Article,Categorie
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class ArticleFrom(forms.ModelForm):
    tynyFiel = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}))
    class Meta:
        model = FlatPage
        fields='__all__'