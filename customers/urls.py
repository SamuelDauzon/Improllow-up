# coding: utf-8
from django.conf.urls import include, url

from .cbv_base.CreateView import CreateViewCustom
from .cbv_base.DeleteView import DeleteViewCustom
from .cbv_base.UpdateView import UpdateViewCustom
from .cbv_base.ListView import ListViewCustomOrderBy
from .cbv_base.DetailView import DetailViewCustom
from .models import Customer
from .views import detail

urlpatterns = [
    url(r'^(list)?$', 
        ListViewCustomOrderBy.as_view(
            model=Customer, 
            cbv_order_by="created", 
            url_delete_name = "customers:delete", 
            url_update_name = "customers:update", 
            url_create_name = "customers:create", 
            url_list_name = "customers:list", 
            url_detail_name = "customers:detail", 
            template_name="cbv/ListViewCustom.html",
        ), 
        name='list'
    ),
    url(r'^create$', 
        CreateViewCustom.as_view(
            model=Customer, 
            success_url="customers:list", 
            url_name="customers:create", 
            template_name="cbv/CreateViewCustom.html",
            fields={'corporate_name', }
        ),
        name='create'
    ),
    url(r'^update-(?P<pk>\d+)$', 
        UpdateViewCustom.as_view(
            model=Customer, 
            success_url="customers:list", 
            url_name="customers:update", 
            template_name="cbv/UpdateViewCustom.html"
        ), 
        name='update'
    ),
    url(r'^delete-(?P<pk>\d+)$', 
        DeleteViewCustom.as_view(
            model=Customer, 
            url_name="customers:delete", 
            success_url="customers:list", 
            template_name="cbv/DeleteViewCustom.html"
        ), 
        name='delete'
    ),
    url(r'^detail-(?P<pk>\d+)$', detail, name="detail"),

]