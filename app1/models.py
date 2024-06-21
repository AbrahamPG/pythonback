from django.db import models

# Create your models here.
class App1(models.Model):
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    pais = models.CharField(max_length=27, default='')
    dni = models.IntegerField(max_length=8, default='00000000')
    vigente = models.BooleanField(default=True)

    def __str__(self):
        return "{} de {} tiene {} años".format(self.nombre,self.pais,self.edad)