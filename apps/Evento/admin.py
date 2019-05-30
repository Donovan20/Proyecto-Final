# Django
from django.contrib import admin

# Modelos
from apps.Evento.models import Evento
from apps.Evento.models import ComentarioEvento

# Register your models here.
admin.site.register(Evento)
admin.site.register(ComentarioEvento)