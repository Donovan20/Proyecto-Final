# Django
from django.utils.translation import ugettext_lazy as _
from django import forms

# Rest
from rest_framework import serializers

# Modelos
from apps.Evento.models import Evento

class EventoSeri(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

    def validate_foto(self, foto):
        if foto.name.endswith('.jpg') or foto.name.endswith('.jpeg') or foto.name.endswith('.png'):
            return foto
        else:
            raise serializers.ValidationError({
                'foto': _('¡Formato de archivo invalido!.\n Solo fotos con extencion .jpg, .jpeg o png.')
            })

class Eventos(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id','usuario','descripcion','foto','fecha','hora','nombre')

    def validate_foto(self, foto):
        if foto.name.endswith('.jpg') or foto.name.endswith('.jpeg') or foto.name.endswith('.png'):
            return foto
        else:
            raise serializers.ValidationError({
                'foto': _('¡Formato de archivo invalido!.\n Solo fotos con extencion .jpg, .jpeg o png.')
            })
