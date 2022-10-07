from django.db import models
from .validators import validar_telefono
from .validators import validar_correo

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length=3,primary_key=True)
    nombre = models.CharField(max_length = 50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.nombre

class Sexos(models.TextChoices):
    MASCULINO = 'M','MASCULINO'
    FEMENINO = 'F','FEMENINO'

class Estudiante(models.Model):
    ci = models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    correo = models.EmailField(max_length=250, unique=True, validators=[validar_correo])
    telefono = models.CharField( max_length=8, unique=True, validators=[validar_telefono])
    sexo = models.CharField(max_length=1,choices = Sexos.choices, default='M')
    carrera = models.ForeignKey(
        Carrera,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.nombre,self.apellidoPaterno,self.apellidoMaterno) 

    def __str__(self):
        cadena = self.nombreCompleto() 
        return cadena

class Curso(models.Model):
    codigo = models.CharField(max_length=6,primary_key=True)  
    nombre = models.CharField(max_length=30)
    docente = models.CharField(max_length=200)

    def __str__(self):
        cadena = "{0} ({1})"
        return cadena.format(self.nombre,self.docente)

class Matricula(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    curso = models.ForeignKey(
        Curso,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    fechaMatricula = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        cadena = "{0} matriculado en el curso {1} / Fecha: {2}"
        fechaStr = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return cadena.format(self.estudiante.nombreCompleto(),self.curso,fechaStr)