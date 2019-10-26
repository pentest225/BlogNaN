from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.

from allConfig.models import Social
class MyUser(AbstractUser):
    specialite = models.ManyToManyField('Specialite', related_name='user_specialiste')
    image = models.ImageField(upload_to='utilisateur/')
    groups = models.ManyToManyField(Group,related_name="utilisateur_groups")
    user_permissions = models.ManyToManyField(Permission,related_name="utilisateur_permissions")
    description = models.TextField()
    specialite = models.ManyToManyField('Specialite',related_name='user_specialite')
    social = models.ManyToManyField(Social, related_name='social_user')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for utilisateur."""
        verbose_name = 'utilisateur'
        verbose_name_plural = 'utilisateurs'

    def __str__(self):
        """Unicode representation of utilisateur."""
        return '{}'.format(self.username) # TODO

class Specialite(models.Model):
    specialiste = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    
