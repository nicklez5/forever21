from django.db import models
from django.conf import settings
 
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=400,null=True,blank=True)
    #phone = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.user)