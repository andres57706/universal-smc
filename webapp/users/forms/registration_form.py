from django import forms
from django.contrib.auth.forms import UserCreationForm

from ..models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ("email",)