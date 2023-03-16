from django.db import models

# Create your models here.

class UserModel(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)