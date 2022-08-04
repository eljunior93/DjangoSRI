from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre

class DatosEmpresa(models.Model):
    ruc = models.CharField(max_length=20)
    clave = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.ruc