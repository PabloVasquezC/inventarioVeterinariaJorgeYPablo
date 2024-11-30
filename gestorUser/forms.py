from django import forms
from django.contrib.auth.models import User

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Personaliza según lo que quieras editar