# coding: UTF-8
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.contrib import messages

class CreateViewBase(CreateView):
	url_name = ""
		
class CreateViewCustom(CreateViewBase):
	template_name = 'base/templates/cbv/base/CreateViewCustom.html'
	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Ajout effectué')
		return reverse(self.success_url)
	def get_context_data(self, **kwargs):
		context = super(CreateViewCustom, self).get_context_data(**kwargs)
		model_name = self.model._meta.verbose_name.title()
		context['model_name'] = model_name
		context['url_name'] = self.url_name
		return context