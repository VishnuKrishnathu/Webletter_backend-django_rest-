from django.db import models

# Create your models here.

class UsernameStorage(models.Model):
    userdata = models.ForeignKey('webletter_api.BlogUsers', null=True, on_delete= models.SET_NULL)
    username = models.CharField(max_length=25, unique=True)