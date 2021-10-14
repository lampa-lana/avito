from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UsernameField, UserCreationForm
)
from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.forms import Form
from django.utils.translation import gettext, gettext_lazy as _


class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username',
                                                           'class': 'login-form'}))

    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Пароль', 'class': 'password-form'}),
    )

    error_messages = {
        'invalid_login': "Введен неправильный логин или пароль",
    }


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'login-password',
        }),
    )

    password2 = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'login-password',
        }),
        help_text='Введите тот же пароль, что и выше'
    )

    error_messages = {
        'password_mismatch': 'Пароли не совпадают'
    }

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('email должен быть уникальным')
        return email
