from django.conf.urls import include, url

from customers.cbv_base.DeleteView import DeleteViewCustom
from customers.cbv_base.UpdateView import UpdateViewCustom
from customers.cbv_base.ListView import ListViewCustomOrderBy
from customers.cbv_base.DetailView import DetailViewCustom
from .cbv import UserCreate
from .models import UserProfile
from .forms import UserForm, UserFormNoPassw
from .views import detail, repartition_project, export_csv, repartition_temps

urlpatterns = [
    url(r'^(list)?$',
        ListViewCustomOrderBy.as_view(
            model=UserProfile,
            cbv_order_by="first_name",
            url_delete_name = "users:delete",
            url_update_name = "users:update",
            url_create_name = "users:create",
            url_list_name = "users:list",
            url_detail_name = "users:detail",
            template_name="cbv/ListViewCustom.html"
        ),
        name='list'
    ),
    url(r'^create$',
        UserCreate.as_view(
            model=UserProfile,
            success_url="users:list",
            url_name="users:create",
            form_class=UserForm,
            template_name="cbv/CreateViewCustom.html"
        ),
        name='create'
    ),
    url(r'^update-(?P<pk>\d+)$',
        UpdateViewCustom.as_view(
            model=UserProfile,
            success_url="users:list",
            url_name="users:update",
            form_class=UserFormNoPassw,
            template_name="cbv/UpdateViewCustom.html"
        ),
        name='update'
    ),
    url(r'^delete-(?P<pk>\d+)$',
        DeleteViewCustom.as_view(
            model=UserProfile,
            url_name="users:delete",
            success_url="users:list",
            template_name="cbv/DeleteViewCustom.html"
        ),
        name='delete'
    ),
    url(r'^detail-(?P<pk>\d+)$', detail, name='detail'),
    url(r'^repartition_temps-(?P<pk>\d+)$', repartition_temps, name='repartition_temps'),
    url(r'^repartition_temps-(?P<pk>\d+)_(?P<start>(\d+-\d+-\d+)?)_(?P<end>(\d+-\d+-\d+)?)$', repartition_temps, name='repartition_temps'),
    url(r'^repartition_project-(?P<pk>\d+)$', repartition_project, name='repartition_project'),
    url(r'^repartition_project-(?P<pk>\d+)_(?P<start>(\d+-\d+-\d+)?)_(?P<end>(\d+-\d+-\d+)?)$', repartition_project, name='repartition_project'),
    url(r'^export-csv-(?P<pk>\d+)$', export_csv, name='export_csv'),
    url(r'^export-csv-(?P<pk>\d+)_(?P<start>(\d+-\d+-\d+)?)_(?P<end>(\d+-\d+-\d+)?)$', export_csv, name='export_csv'),
]