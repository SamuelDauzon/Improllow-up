# coding:utf-8
from django.contrib.auth import authenticate
from django import forms
from bootstrap3_datetime.widgets import DateTimePicker

from projects.forms import FormBase, ModelFormBase
from .models import UserProfile

class FormConnection(FormBase):
    """
    Formulaire de connexion
    """
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(FormConnection, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Authentification incorrecte")
        return self.cleaned_data

class UserFormNoPassw(ModelFormBase):
    """
    Mise à jour d'un compte
    """
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'boss', 'hiring_date')
        widgets = {
            'hiring_date': DateTimePicker(
                options = {
                    "format": "YYYY-MM-DD",
                    "pickTime": False
                }
            )
        }

class UserForm(UserFormNoPassw):
    """
    Création d'un compte
    """
    class Meta:
        model = UserFormNoPassw.Meta.model
        fields = UserFormNoPassw.Meta.fields + ('password',)
        widgets = UserFormNoPassw.Meta.widgets

