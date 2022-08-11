from django.db import models


# Create your models here.
class User(models.Model):
    roll_number = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
