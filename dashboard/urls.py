from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$',views.dashboard ,name='home'),
    url(r'add-task/',views.add_task,name='task'),
    url(r'view-task/(?P<pk>[0-9a-z-]+)/$',views.view_task,name='view_task'),
    url(r'edit-task/(?P<pk>[0-9a-z-]+)/$',views.edit_task,name='edit_task'),
    url(r'delete-task/(?P<pk>[0-9a-z-]+)/$',views.delete_task,name='delete'),

]







