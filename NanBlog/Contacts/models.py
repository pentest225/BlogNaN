from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Les Souscription au site"
        verbose_name_plural = "Les Souscription au site"
    def __str__(self):
        return '{}'.format(self.email)




class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sujet = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    class Meta:
            verbose_name = "Message Visiteur"
            verbose_name_plural = "Message Visiteur"
    def __str__(self):
        return '{}'.format(self.nom)