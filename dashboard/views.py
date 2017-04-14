# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView ,DetailView, UpdateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import PermissionDenied
from django.views.generic.edit import DeleteView
from .models import *
from  .forms import *

class DashboardView(TemplateView):
	template_name = "dashboard.html"

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(self.__class__, self).get_context_data(**kwargs)
		alltodo = todotask.objects.filter(hidestatus='1').order_by('-id')
		context['todo'] = alltodo
		return context



class addTaskView(FormView):
	template_name = 'add_task.html'
	form_class = addTaskForm
	success_url = '/dashboard/'

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(self.__class__, self).get_context_data(**kwargs)
		alltodo = todotask.objects.filter(addedBy=self.request.user).order_by('-id')
		context['todo'] = alltodo
		return context

	def form_valid(self, form):

		obj = form.save(commit=False)
		obj.addedBy = self.request.user
		obj.save()
		return super(self.__class__, self).form_valid(form)



class viewTaskView(TemplateView):
	template_name = "view.html"

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)


	def get_context_data(self, **kwargs):
		context = super(self.__class__, self).get_context_data(**kwargs)
		taskid =  self.kwargs['pk']
		particulartask = todotask.objects.get(pk=taskid)
		alltodo = todotask.objects.filter(addedBy=self.request.user).order_by('-id')
		context['todo'] = alltodo
		context['viewtask'] = particulartask

		return context



class userCheckMixin(object):

	def dispatch(self,*args, **kwargs):
		taskid = self.kwargs['pk']


		obj = todotask.objects.get(pk=taskid)
		if obj.addedBy.id != self.request.user.id:
			raise PermissionDenied("You are only allowed to edit your own task")
		return super(userCheckMixin, self).dispatch(*args, **kwargs)



class editTaskView(userCheckMixin,UpdateView):
	model = todotask
	form_class = EditTaskForm
	template_name = 'edit_task.html'
	success_url = '/dashboard'


class taskDeleteView(userCheckMixin,DeleteView):
    model = todotask
    success_url = '/dashboard'
    template_name = 'delete_task.html'






dashboard       = DashboardView.as_view()
add_task        = addTaskView.as_view()
view_task       = viewTaskView.as_view()
edit_task       = editTaskView.as_view()
delete_task     = taskDeleteView.as_view()