from django.contrib.auth.forms import BaseUserCreationForm, ReadOnlyPasswordHashField
from django.forms import forms , ModelForm

from .models import User


class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = (
            'phone_number',
            'email',
            'is_active',
            'is_staff',
            'is_superuser'
        )


class CustomUserChangeForm(ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'phone_number',
            'email',
            'first_name',
            'last_name',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )
