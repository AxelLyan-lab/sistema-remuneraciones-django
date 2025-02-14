#Logica de Negocio y contenedores con las peticiones HTTP
import bcrypt
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AfpSerializer, UserSerializer
from .models import User,UserTipo
from datetime import datetime
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


#Registro Del Usuario , 1.-deserialización de los datos , 2.-validacion de los datos , 3.- guardar los datos
class RegistroUsuario(APIView):
    def post(self, request):
        # Recibir los datos del cuerpo de la solicitud
        username = request.data.get("username")
        contrasena = request.data.get("contrasena")
        correo = request.data.get("correo")
        
        # Validaciones
        if not username or not contrasena or not correo:
            return Response({"error": "Faltan campos"}, status=status.HTTP_400_BAD_REQUEST)
        
         # Validar que el username no contenga espacios
        if ' ' in username:
            return Response({"error": "El nombre de usuario no puede contener espacios"}, status=status.HTTP_400_BAD_REQUEST)

        
        tipo_user = UserTipo.objects.get(id_user_tipo=1)  # Obtener la instancia completa
        
        # Hash de la contraseña
        contrasena_hashed = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Crear el usuario
        try:
            user = User.objects.create(
                username=username,
                contrasena_hashed=contrasena_hashed,
                correo=correo,
                fecha_creacion=datetime.now().date(),
                estado=1,  # Suponiendo que '1' representa un estado activo
                id_tipo_user = tipo_user  # Asignar la instancia,  # Suponiendo que el tipo de usuario es el id 1
            )
            user.save()
            return Response({"mensaje": "Usuario registrado correctamente"}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return JsonResponse({"error": "Ya existe un usuario con ese correo electrónico."}, status=400)
        except Exception as e:
            return Response({"error": f"Error al registrar usuario: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#class UserLogin(APIView):

class LoginUsuario(APIView):
    def post(self, request):
        # Obtener los datos del formulario
        username_or_email = request.data.get("username")
        contrasena = request.data.get("contrasena")
        print(request.data)  # Esto te mostrará el JSON recibido en la consola

        # Validar si ambos parámetros están presentes
        if not username_or_email or not contrasena:
            return Response({"error": "Por favor, proporcione el nombre de usuario y la contraseña."}, status=status.HTTP_400_BAD_REQUEST)

        # Buscar usuario por username o correo
        user = User.objects.filter(username=username_or_email).first() or User.objects.filter(correo=username_or_email).first()

        if not user:
            return Response({"error": "Usuario o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
                # Comparar la contraseña hasheada
        if not bcrypt.checkpw(contrasena.encode('utf-8'), user.contrasena_hashed.encode('utf-8')):
            return Response({"error": "Usuario o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        
        elif not user.estado == 1:
            return Response({"error": "El usuario está inactivo"}, status=status.HTTP_403_FORBIDDEN)

        # Generar JWT
        # Crear manualmente los tokens JWT
        refresh = RefreshToken()
        access_token = refresh.access_token

        # Agregar manualmente la información del usuario al token
        refresh["user_id"] = user.id_user  # O el campo que corresponda a tu identificador único
        access_token["user_id"] = user.id_user

        # Responder con los tokens
        return Response({
            'access': str(access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)


#Lista de Usuarios 
class UserListView(APIView):
    #Por ahora no permission_classes = [IsSpecificRole]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


