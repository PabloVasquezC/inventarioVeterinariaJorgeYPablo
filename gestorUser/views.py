from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import EditUserForm

class EditUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditUserForm
    template_name = "registration/edit_user.html"
    success_url = reverse_lazy("index")  # Cambia "index" si tu URL principal es distinta

    def get_object(self):
        # Devuelve el usuario autenticado para evitar editar otros usuarios
        return self.request.user
    
# Create your views here.

@login_required

def index(request):
    return render(request, template_name='index.html')

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "¡Usuario creado exitosamente!"