# coding:utf-8
import datetime

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

class TimeRangeForm(FormBase):
    """
    Formulaire de choix d'une période
    """
    start = forms.DateField(
        initial = datetime.date.today, 
        label = "Début", 
        )
    end_date = datetime.datetime.now() - datetime.timedelta(days=7)
    end = forms.DateField(
        initial = end_date, 
        label = "Fin",
        )
    def __init__(self, *args, **kwargs):
        super(TimeRangeForm, self).__init__(*args, **kwargs)
        end_date = datetime.datetime.now() - datetime.timedelta(days=7)
        start_date = datetime.datetime.now().strftime('%Y-%m-%d')

        self.fields['start'].widget.attrs.update(
            {'ng-model' : 'start', 'placeholder' : 'AAAA-MM-DD'}
            )
        self.fields['end'].widget.attrs.update(
            {'ng-model' : 'end', 'placeholder' : 'AAAA-MM-DD'}
            )


