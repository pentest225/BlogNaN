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

        verbose_name = "Les Categories d'articles"
        verbose_name_plural = "Les Categorie d'articles"

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

        verbose_name = 'Les Tags Du blog'
        verbose_name_plural = 'Les Tags Du Blog'

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
    vue = models.PositiveIntegerField()
    is_archive=models.BooleanField(default=False, blank=True, null=True)
    image_single = models.ImageField(upload_to='blog/single')
    status = models.BooleanField(default=False,null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Les Articles du Blogs'
        verbose_name_plural = 'Les Articles du Blogs'

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
    class Meta:
        """Meta definition for Categorie."""

        verbose_name = "Les Commentaires d'articles"
        verbose_name_plural = "Les Commentaires d'articles"


class ResponseCommentaire(models.Model):
    comment = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name='response')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_response_comment')
    message = HTMLField('message', default="null")
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Categorie."""

        verbose_name = " Les Reponses de Commentaire"
        verbose_name_plural = " Les Reponses de Commentaire"

class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_like')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_like')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Categorie."""

        verbose_name = " Les Likes d'Article"
        verbose_name_plural = " Les Likes d'Article"
    
class DisLike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='Dislike')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_dislike')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Categorie."""

        verbose_name = " Les DisLikes d'Article"
        verbose_name_plural = " Les  DisLikes d'Article "
    
class DemandeAdesion(models.Model):
    user_id=models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='user_demande')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Categorie."""

        verbose_name = "Demande de Membre"
        verbose_name_plural = "Demande de Membre"
