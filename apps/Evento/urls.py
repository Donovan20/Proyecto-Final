# Django
from django.urls import path

from apps.Evento.views import nuevo_evento,publicacionEvento,comentarEvento,eventos

app_name='Evento'
urlpatterns = [
	path('', eventos, name='adopciones'),
    path('comentarios/', publicacionEvento, name='publicacionA'),
    path('nuevo/', nuevo_evento, name='nuevo_evento'),
    path('comentar/', comentarEvento, name='comentarA'),

]
	