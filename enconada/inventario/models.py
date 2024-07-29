from django.db import models
from .validators import mayor_edad
# Create your models here. 
class Genero(models.TextChoices):
    male = "M", "Masculino"
    female = "F", "Femenino"
class Persona(models.Model):
    ci = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    edad = models.IntegerField(validators=([mayor_edad]))
    genero = models.CharField(
        max_length=2,
        choices=Genero.choices,
        default=Genero.male)
    def __str__(self):
        return self.nombre
class Arrendador(models.Model):
    id_arrendador = models.CharField(max_length=10, unique=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    def __str__(self):
        return self.persona.nombre
class Arrendatario(models.Model):
    id_arrendatario = models.CharField(max_length=10, unique=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    arrendador = models.ForeignKey(Arrendador, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.persona.nombre

class Contrato(models.Model):
    idContrato = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=100)
    inicio_contrato = models.DateTimeField()
    fin_contrato = models.DateField()
    costo_alquiler = models.IntegerField()
    arrendador = models.ForeignKey(Arrendador, on_delete=models.CASCADE)
    arrendatario = models.ForeignKey(Arrendatario, on_delete=models.CASCADE)
    def __str__(self):
        return "#"+self.idContrato+" "+ self.arrendatario.persona.nombre

