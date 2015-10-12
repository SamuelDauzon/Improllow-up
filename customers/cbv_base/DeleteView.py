# coding: UTF-8
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView
from django.contrib import messages


class DeleteViewBase(DeleteView):
	url_name = ""
	template_name = 'base/templates/cbv/base/DeleteViewCustom.html'
	

class DeleteViewCustom(DeleteViewBase):
	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Suppression effectuée')
		return reverse(self.success_url)
	def get_context_data(self, **kwargs):
		context = super(DeleteViewCustom, self).get_context_data(**kwargs)
		model_name = self.model._meta.verbose_name.title()
		context['model_name'] = model_name
		context['url_name'] = self.url_name
		return context