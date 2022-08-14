from django.db import models
from tinymce.models import HTMLField

"""
    google font: Open Sens, lato, nunito
"""
class Convention(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        abstract = True

class Banner(Convention):
    picture = models.FileField(max_length=100, upload_to="img_banner")
    libele = HTMLField()
    

    def __str__(self):
        return self.libele

class ReseauSocial(Convention):
    name= models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    link = models.URLField(null=True)
    

    def __str(self):
        return self.name

class Site(Convention):
    name = models.CharField(max_length=30)
    picture = models.FileField(upload_to="img_site")
    email = models.EmailField(max_length=100)
    phone = models.PositiveIntegerField()
    copyright = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name


class Service(Convention):
    name = models.CharField(max_length=50)
    picture = models.FileField(upload_to="img_service")
    libele = HTMLField()
    description = models.TextField()
    order = models.IntegerField()
    

    def __str__(self):
        return self.name


class About(Convention):
    description = models.TextField()
    

    def __str__(self):
        return self.description

class UnderService(Convention):
    name = models.CharField(max_length=50)
    picture = models.FileField(upload_to="img_under_site")
    libele = HTMLField()
    description = models.TextField()
    order =models.IntegerField()
    price = models.CharField(max_length=6)
    

    def __srt__(self):
        return self.name