from datetime import *
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, UserManager
# Create your models here.
class Men_Shirt(models.Model):
    img_url = models.URLField(max_length=500)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
   

#
class Men_Jacket(models.Model):
    img_url = models.URLField(max_length=500)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

class Men_Pants(models.Model):
    img_url = models.URLField(max_length=500)
    waist_size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

class Men_Joggers(models.Model):
    img_url = models.URLField(max_length=500)
    waist_size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

class Glasses(models.Model):
    img_url = models.URLField(max_length=500)
    price = models.FloatField()
    name = models.CharField(max_length=100)

class Earring(models.Model):
    img_url = models.URLField(max_length=500)
    price = models.FloatField()
    name = models.CharField(max_length=100)

class Necklace(models.Model):
    img_url = models.URLField(max_length=500)
    price = models.FloatField()
    name = models.CharField(max_length=100)

class Women_Shirt(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    img_url = models.URLField(max_length=500)
    name = models.CharField(max_length=100)

class Women_Jacket(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    img_url = models.URLField(max_length=500)
    name = models.CharField(max_length=100)

class Women_Pants(models.Model):
    img_url = models.URLField(max_length=500)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

class Women_Joggers(models.Model):
    img_url = models.URLField(max_length=500)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    mens_shirt = models.ForeignKey(Men_Shirt, on_delete=models.CASCADE)
    mens_jacket = models.ForeignKey(Men_Jacket, on_delete=models.CASCADE)
    mens_pants = models.ForeignKey(Men_Pants,on_delete=models.CASCADE)
    mens_joggers = models.ForeignKey(Men_Joggers, on_delete=models.CASCADE)
    glasses = models.ForeignKey(Glasses, on_delete=models.CASCADE)
    earring = models.ForeignKey(Earring, on_delete=models.CASCADE)
    necklace = models.ForeignKey(Necklace, on_delete=models.CASCADE)
    women_shirt = models.ForeignKey(Women_Shirt, on_delete=models.CASCADE)
    women_jacket = models.ForeignKey(Women_Jacket, on_delete=models.CASCADE)
    women_pants = models.ForeignKey(Women_Pants,on_delete=models.CASCADE)
    women_joggers = models.ForeignKey(Women_Joggers,on_delete=models.CASCADE)


