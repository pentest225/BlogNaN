from django.db import models

# Create your models here.

from allConfig.models import Social
class Utilisateur(models.Model):
    specialite = models.ManyToManyField('Specialite', related_name='user_specialiste')
    nom = models.CharField(max_length=250)
    image = models.ImageField(upload_to='utilisateur/')
    message = models.TextField()
    specialite = models.CharField(max_length=250)
    social = models.ManyToManyField(Social, related_name='social_user')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Specialite(models.Model):
    specialiste = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)