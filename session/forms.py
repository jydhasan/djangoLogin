from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Form definition for SignUp."""

    class Meta:
        """Meta definition for SignUpform."""

        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)
