from django import forms
from .models import Article,Categorie
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class ArticleFrom(forms.ModelForm):
    contenu = forms.CharField(widget=TinyMCE())
    class Meta:
        model = Article
        fields='__all__'
    class Media:
        js = ('/static/tinymce/js/prism.js','/static/tinymce/js/tinymce/tinymce.min.js')