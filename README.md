# BlogNaN
 Projet de goupe creation de Blog 

# Application Blog
```python
from tinymce import HTMLField
from django.contrib.auth.models import User
from utilisateur.models import Membre, Visiteur

class Categorie(models.Model):
    """Model definition for Categorie."""
    nom = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

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
    # TODO: Define fields here

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
    auteur = models.ForeignKey(Membre, on_delete=models.CASCADE, related_name='article_auteur')
    tag = models.ManyToManyField(Tag, related_name='article_tag')
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    contenu = HTMLField('Content', default="null")
    image_single = models.ImageField(upload_to='blog/single')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre

class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_commentaire')
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='user_comment')
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sujet = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)


class ResponseCommentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='response')
    user_id = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='user_comment_response')
    message = models.TextField()
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
    like = models.IntegerField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
```

# Application Message
```python
class Newsletter(models.Model):
    email = models.EmailField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sujet = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
```
# Application Config

## au niveau de contact cette classe allinfo
```python
class AllInfo(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class HeaderFront(models.Model):
    logo = models.ImageField(upload_to='entreprise/')
    image = models.ImageField(upload_to='blog/')
    titre = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class FooterFront(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Social(models.Model):
	# TODO: Define fields here
	choice=[('FB','facebook'),('TW','twitter'),('INS','instagram'),('GOO','google')]
	name = models.CharField(max_length=100,choices=choice)
	lien = models.URLField(max_length=200)
	status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)
	@property
	def font(self):
		print(self.name)
		if self.name == 'FB':
			font = 'icon-facebook'
		elif self.name == 'TW':
			font ='icon-twitter'
		elif self.name == 'INS':
			font ='icon-instagram'
		elif self.name == 'GOO':
			font ='icon-google-plus'
		return font
	class Meta:
	    verbose_name = "Social"
	    verbose_name_plural = "Socials"

	def __str__(self):
	    return '{}'.format(self.name)

class LocationMap(models.Model):
    map = URLField()
    status = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

class Copyright(models.Model):
    titre = HTMLField('content')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Instagram(models.Model):
    image = models.ImageField(upload_to='instagram/')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

```

# Application Utilisateur

```python
from config.models import Social

class Utilisateur(models.Model):
    specialite = models.ManyToManyField('Specialite', related_name='user_specialiste')
    nom = models.CharField(max_length=250)
    image = models.ImageField(upload_to='utilisateur/')
    message = models.TextField()
    specialite = models.CharField()
    social = models.ManyToManyField('Social', related_name='social_config')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Specialite(models.Model):
    specialiste = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

  ```
