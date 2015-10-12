# coding: UTF-8
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import Group

from customers.cbv_base.CreateView import CreateViewCustom
from customers.cbv_base.DeleteView import DeleteViewCustom
from customers.cbv_base.DetailView import DetailViewCustom
from customers.cbv_base.UpdateView import UpdateViewCustom
from .forms import FormConnection, UserForm

class UserPasswordUpdate(UpdateViewCustom):
    def get_object(self, queryset=None):
        return self.request.user
    def form_valid(self, form):
        """
        Permet de hasher le mot de passe utilisateur
        """
        self.object = form.save()
        if self.object.id == self.request.user.id:
            self.object.set_password(self.object.password)
            self.object.save()
        self.object.save()
        return super(UserUpdate, self).form_valid(form)


class UserCreate(CreateViewCustom):
    def form_valid(self, form):
        """
        Permet de hasher le mot de passe utilisateur
        """
        self.object = form.save()
        self.object.set_password(self.object.password)
        return super(UserCreate, self).form_valid(form)
    def get_success_url(self):
        return reverse('users:list')
    def get_context_data(self, **kwargs):
        context = super(UserCreate, self).get_context_data(**kwargs)
        context['form_connection'] = FormConnection()
        return context


