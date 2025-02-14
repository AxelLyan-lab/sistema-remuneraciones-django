"""
URL configuration for remunintranet project.
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import RegistroUsuario,LoginUsuario
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
        #Entrar Al Panel De Administrador
        path('admin/', admin.site.urls),
        #Metodo Post de Registro de Usuario
        path('api/register/', RegistroUsuario.as_view(), name='register'),
        path('api/login/', LoginUsuario.as_view(), name='login'),
]


""" urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('api/afp/',AfpList.as_view(),name='lista_afp').
    path('api/afps/', AfpListView.as_view(), name='listar_afps'),
]
    """ 