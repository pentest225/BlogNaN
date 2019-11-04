from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.
from allConfig.models import Social



class Specialite(models.Model):
    specialiste = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
class MyUser(AbstractUser):
    image = models.ImageField(upload_to='utilisateur/')
    groups = models.ManyToManyField(Group,related_name="Type_de_compte")
    # user_permissions = models.ManyToManyField(Permission,related_name="utilisateur_permissions")
    description = models.TextField()
    specialite = models.ManyToManyField(Specialite,related_name='user_specialite')
    social = models.ManyToManyField(Social, related_name='social_user')
    status = models.BooleanField(default=True,null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['email', 'last_name', 'first_name']

    class Meta:
        """Meta definition for utilisateur."""
        verbose_name = 'utilisateur'
        verbose_name_plural = 'utilisateurs'
        constraints = [models.UniqueConstraint(fields=['email'], name='unique email')
    ]

    def __str__(self):
        """Unicode representation of utilisateur."""
        return '{}'.format(self.username) # TODO

    
