from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class MeghalayaImages(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="img/")
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class MeghalyaVideos(models.Model):
    name = models.CharField(max_length=150)
    video = models.FileField(upload_to='videos/',blank=True, null=True)  # this is the key addition
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    

class RegionOfMeghalaya(models.Model):
    name = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="img/")
    description = models.TextField(default='',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Festival(models.Model):
    festival_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/")
    description = models.TextField(default='',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.festival_name
    


class TrevalAround(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(upload_to="img/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name