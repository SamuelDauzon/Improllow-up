# coding: utf-8
from django.conf.urls import include, url

from customers.cbv_base.CreateView import CreateViewCustom
from customers.cbv_base.DeleteView import DeleteViewCustom
from customers.cbv_base.UpdateView import UpdateViewCustom
from customers.cbv_base.ListView import ListViewCustomOrderBy
from customers.cbv_base.DetailView import DetailViewCustom
from .models import Task
from .cbv import TaskCreate
from .forms import TaskForm

urlpatterns = [
    url(r'^(list)?$', 
        ListViewCustomOrderBy.as_view(
            model = Task, 
            cbv_order_by = "created", 
            url_delete_name = "tasks:delete", 
            url_update_name = "tasks:update", 
            url_create_name = "tasks:create", 
            url_list_name = "tasks:list", 
            url_detail_name = "tasks:detail", 
            template_name = "cbv/ListViewCustom.html",
        ),
        name = 'list'
    ),
    url(r'^create$', 
        TaskCreate.as_view(
            model=Task, 
            success_url = "tasks:list", 
            url_name = "tasks:create", 
            template_name = "cbv/CreateViewCustom.html",
            form_class = TaskForm,
        ),
        name='create'
    ),
    url(r'^update-(?P<pk>\d+)$', 
        UpdateViewCustom.as_view(
            model=Task, 
            success_url="tasks:list", 
            url_name="tasks:update", 
            template_name="cbv/UpdateViewCustom.html",
            form_class = TaskForm,
        ), 
        name='update'
    ),
    url(r'^delete-(?P<pk>\d+)$', 
        DeleteViewCustom.as_view(
            model=Task, 
            url_name="tasks:delete", 
            success_url="tasks:list", 
            template_name="cbv/DeleteViewCustom.html"
        ), 
        name='delete'
    ),
    url(r'^detail-(?P<pk>\d+)$', 
        DetailViewCustom.as_view(
            model=Task, 
            url_name="tasks:detail", 
            template_name="tasks/detail.html"
        ), 
        name='detail'
    ),
]