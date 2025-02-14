#serializadores para convertir data compleja 

from rest_framework import serializers
from .models import Afp,User

class AfpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afp
        fields = ['id', 'nombre']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'nombre_user', 'contrasena_hashed', 'correo', 'fecha_creacion', 'estado', 'id_tipo_user']