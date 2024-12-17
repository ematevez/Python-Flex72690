from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido}'
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    

    def __str__(self):
        return f'Profesor: {self.nombre}'
    


