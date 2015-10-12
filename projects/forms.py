# coding:utf-8
from django import forms

class FormBase(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FormBase, self).__init__(*args, **kwargs)

class ModelFormBase(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelFormBase, self).__init__(*args, **kwargs)