from django.conf.urls import include, url

from customers.cbv_base.CreateView import CreateViewCustom
from customers.cbv_base.DeleteView import DeleteViewCustom
from customers.cbv_base.UpdateView import UpdateViewCustom
from customers.cbv_base.ListView import ListViewCustomOrderBy
from customers.cbv_base.DetailView import DetailViewCustom
from .models import Project
from .views import detail
# Faire une liste où sont affichées les dernières tâches effectuées de chaque utilisateur

urlpatterns = [
    url(r'^(list)?$', 
        ListViewCustomOrderBy.as_view(
            model=Project, 
            cbv_order_by="name", 
            url_delete_name = "projects:delete", 
            url_update_name = "projects:update", 
            url_create_name = "projects:create", 
            url_list_name = "projects:list", 
            url_detail_name = "projects:detail", 
            template_name="cbv/ListViewCustom.html"
        ), 
        name='list'
    ),
    url(r'^create$', 
        CreateViewCustom.as_view(
            model=Project, 
            success_url="projects:list", 
            url_name="projects:create", 
            template_name="cbv/CreateViewCustom.html",
            fields={'name', 'customer', }
        ),
        name='create'
    ),
    url(r'^update-(?P<pk>\d+)$', 
        UpdateViewCustom.as_view(
            model=Project, 
            success_url="projects:list", 
            url_name="projects:update", 
            template_name="cbv/UpdateViewCustom.html"
        ), 
        name='update'
    ),
    url(r'^delete-(?P<pk>\d+)$', 
        DeleteViewCustom.as_view(
            model=Project, 
            url_name="projects:delete", 
            success_url="projects:list", 
            template_name="cbv/DeleteViewCustom.html"
        ), 
        name='delete'
    ),
    url(r'^detail-(?P<pk>\d+)$', detail, name='detail'),
]