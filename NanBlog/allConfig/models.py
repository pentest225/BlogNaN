from django.db import models
from tinymce import HTMLField
# Create your models here.
class AllInfo(models.Model):
    titre = models.CharField(max_length=250)
    phone=models.CharField(max_length=255,null=True)
    ville=models.CharField(max_length=255,null=True)
    commune=models.CharField(max_length=255,null=True)
    email=models.EmailField(max_length=254,null=True)
    description = models.TextField(null=True)
    contactText=models.TextField()
    icon = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Configuration General du site"
        verbose_name_plural = "Configuration General du site"

class workingHours(models.Model):
    day=models.CharField(max_length=255)
    openHours=models.TimeField()
    closeHours=models.TimeField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class HeaderFront(models.Model):
    logo = models.ImageField(upload_to='entreprise/')
    image = models.ImageField(upload_to='blog/')
    index_title=models.CharField(max_length=255,null=True)
    about_title=models.CharField(max_length=255,null=True)
    cat_title=models.CharField(max_length=255,null=True)
    blog_title=models.CharField(max_length=255,null=True)
    contct_title=models.CharField(max_length=255,null=True)
    titre = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Configuration du header "
        verbose_name_plural = "Configuration du header"

class FooterFront(models.Model):
    titre = models.CharField(max_length=100)
    about_text=models.TextField(null=True)
    newslater_text=models.TextField(null=True)
    folow_text=models.TextField(null=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Configuration du Footer"
        verbose_name_plural = "Configuration du Footer"
    

class Social(models.Model):
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
            font = 'fa fa-facebook'
        elif self.name == 'TW':
            font ='fa fa-twitter'
        elif self.name == 'INS':
            font ='fa fa-instagram'
        elif self.name == 'GOO':
            font ='fa fa-google-plus'
        return font
    class Meta:
        verbose_name = "Configuration des lien sociaux"
        verbose_name_plural = "Configuration des liens sociaux"

    def __str__(self):
        return '{}'.format(self.name)

class LocationMap(models.Model):
    map = models.URLField()
    latitude=models.DecimalField(max_length=10,decimal_places=4,max_digits=10)
    longitude=models.DecimalField(max_length=10,decimal_places=4,max_digits=10)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Configuration de la carte"
        verbose_name_plural = "Configuration de la carte"

class Copyright(models.Model):
    titre = HTMLField('content')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Configuation du Copyright"
        verbose_name_plural = "Configuation du  Copyright"

class Instagram(models.Model):
    image = models.ImageField(upload_to='instagram/')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Image du Footer"
        verbose_name_plural = "Image du Footer"