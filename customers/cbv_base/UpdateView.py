# coding: UTF-8
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from django.contrib import messages


class UpdateViewBase(UpdateView):
	url_name=""
		
		
class UpdateViewCustom(UpdateViewBase):
	template_name = 'base/templates/cbv/base/UpdateViewCustom.html'
	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Modification effectuée')
		return reverse(self.success_url)
	def get_context_data(self, **kwargs):
		context = super(UpdateViewCustom, self).get_context_data(**kwargs)
		model_name = self.model._meta.verbose_name.title()
		context['model_name'] = model_name
		context['url_name'] = self.url_name
		return context