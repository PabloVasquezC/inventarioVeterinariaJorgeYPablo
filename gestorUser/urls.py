from django.urls import path

from gestorUser.views import SignUpView
from gestorUser.views import EditUserView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('editar-perfil/', EditUserView.as_view(), name='edit_user'),
    ]