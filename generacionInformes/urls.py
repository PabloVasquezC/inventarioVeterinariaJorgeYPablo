from django.urls import path

from generacionInformes.views import SignUpView
from generacionInformes.views import EditUserView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('editar-perfil/', EditUserView.as_view(), name='edit_user'),
    ]