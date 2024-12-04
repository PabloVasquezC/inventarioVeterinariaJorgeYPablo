"""
URL configuration for inventarioVeterinariaJorgeYPablo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
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
from tkinter.font import names
from django.contrib import admin
from django.urls import path

from django.urls import path, include
from django.views.generic.base import TemplateView
from generacionInformes.views import index
from registroVentas.views import lista_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", index, name="home"),
    path("usuarios/", include("gestorUser.urls")),
    path("productos/", include("gestorProductos.urls"))

]