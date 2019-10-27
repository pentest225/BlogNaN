from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User
from Utilisateurs.models import MyUser

class Categorie(models.Model):
    """Model definition for Categorie."""
    nom = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom

class Tag(models.Model):
    """Model definition for Tag."""
    nom = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.nom

class Article(models.Model):
    """Model definition for Article."""
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='article_categorie')
    auteur = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='article_auteur')
    tag = models.ManyToManyField(Tag, related_name='article_tag')
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    contenu = HTMLField('contenu')
    image_single = models.ImageField(upload_to='blog/single')
    status = models.BooleanField(default=False,null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre

class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_commentaire')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_comment')
    message = HTMLField('message')
    sujet = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)


class ResponseCommentaire(models.Model):
    comment = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name='response')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_response_comment')
    message = HTMLField('message', default="null")
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Archive(models.Model):
    
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='archive_article')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_like')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_like')
    like = models.IntegerField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
