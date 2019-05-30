# Django
from django.db import models

# Modelos
from apps.Usuario.models import Usuario

# Create your models here.
class Evento(models.Model):
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	fecha = models.DateField(auto_now_add=True)
	hora_inicio = models.TimeField(auto_now=False, auto_now_add=False,default="00:00:am")
	hora_final = models.TimeField(auto_now=False, auto_now_add=False,default="00:00:am")
	lugar = models.CharField(max_length=60)
	descripcion = models.TextField(max_length=360)
	foto = models.ImageField(
		upload_to = 'Eventos',
		blank = True,
		null = True
	)

class ComentarioEvento(models.Model):
	evento = models.ForeignKey(Evento, null=True, blank=True, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	comentario = models.TextField(max_length=160)