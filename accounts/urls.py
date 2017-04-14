from django.conf.urls import url
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm




urlpatterns = [
	url(r'^$',views.login,name='login'),
	url(r'register/',CreateView.as_view(template_name='register.html',form_class=UserCreationForm,success_url='/'),name='register'),
	url('logout/',views.logout,name='logout'),

]