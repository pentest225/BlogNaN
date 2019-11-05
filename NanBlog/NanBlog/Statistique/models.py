from django.db import models

# Create your models here.


class Client(models.Model):
    ip = models.GenericIPAddressField()
    continent = models.CharField(max_length=160)
    pays = models.CharField(max_length=160)
    ville = models.CharField(max_length=160)
    reseau =  models.CharField(max_length=160)
    longitude = models.FloatField()
    latitude = models.FloatField()
    page = models.CharField(max_length=160)
    date_visite =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.adresse_ip

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'