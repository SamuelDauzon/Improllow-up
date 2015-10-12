# coding: utf-8
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import Group

from customers.cbv_base.CreateView import CreateViewCustom
from customers.cbv_base.DeleteView import DeleteViewCustom
from customers.cbv_base.DetailView import DetailViewCustom
from customers.cbv_base.UpdateView import UpdateViewCustom

class TaskCreate(CreateViewCustom):
    def form_valid(self, form):
        """
        Permet de hasher le mot de passe utilisateur
        """
        self.object = form.save()
        self.object.user_add = self.request.user
        self.object.save()
        return super(TaskCreate, self).form_valid(form)


