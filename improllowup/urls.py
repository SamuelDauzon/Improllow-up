from django.conf.urls import include, url
from django.contrib import admin

from users.views import logout_user, connection

urlpatterns = [
    url(
        r'^customers/', 
        include('customers.urls', namespace="customers", app_name='customers')
    ),
    url(
        r'^users/', 
        include('users.urls', namespace="users", app_name='users')
    ),
    url(
        r'^projects/', 
        include('projects.urls', namespace="projects", app_name='projects')
    ),
    url(
        r'^tasks/', 
        include('tasks.urls', namespace="tasks", app_name='tasks')
    ),
    
    url(r'^$', connection, name="login"),
    url(r'^logout$', logout_user, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
]
