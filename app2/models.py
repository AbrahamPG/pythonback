from django.db import models

# Create your models here.
class App2(models.Model):
    nombre= models.CharField(max_length=30)