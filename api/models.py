from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class pacientes (models.Model):

    nombre               = models.CharField(max_length=50, null=False)
    edad                 = models.IntegerField(max_length=10, null=False,validators=[MinValueValidator(0), MaxValueValidator(190)])
    correo               = models.EmailField(max_length=60, blank=True)
    direccion            = models.CharField(max_length=100, null=False)
    antecedentes_medicos = models.TextField( null=False)





class especialidades (models.Model):

    nombre      = models.CharField(max_length=50, null=False)
    area        = models.CharField(max_length=10, null=False)
    experiencia = models.IntegerField(max_length=60, blank=True)


class doctores (models.Model):

    nombre         = models.CharField(max_length=50, null=False)
    edad           = models.IntegerField(max_length=10, null=False)
    correo         = models.EmailField(max_length=60, blank=True)
    especialidad   = models.ForeignKey(especialidades, null = False, on_delete = models.CASCADE, related_name='doctores')
    años_laborados = models.IntegerField( null=False)


class especialidades_x_doctores (models.Model):

    doctor       = models.ForeignKey(doctores, null = False, on_delete = models.CASCADE, related_name='doctores')
    especialidad = models.ForeignKey(especialidades, null = False, on_delete = models.CASCADE, related_name='especialidades')


class citas (models.Model):

    fecha  = models.DateField(max_length=50, null=False)
    hora   = models.TimeField(max_length=10, null=False)
    motivo = models.TextField(max_length=300, blank=True)
    doctor =models.ForeignKey(doctores, null = False, on_delete = models.CASCADE, related_name='citas')


