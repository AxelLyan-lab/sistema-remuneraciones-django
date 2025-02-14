from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from remunintranet.models import User  # Importa tu modelo personalizado

class EmailOrUsernameModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Buscar usuario por username o correo
            user = User.objects.get(username=username) if '@' not in username else User.objects.get(correo=username)
        except User.DoesNotExist:
            return None

        # Comparar la contraseña ingresada con la almacenada
        if check_password(password, user.contrasena_hashed):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id_user=user_id)
        except User.DoesNotExist:
            return None
