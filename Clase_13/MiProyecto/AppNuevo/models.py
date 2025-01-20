from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    correo = models.EmailField()
    
    
    def __str__(self):
        return self.nombre
