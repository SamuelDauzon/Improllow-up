# coding: UTF-8
from django.views.generic import DetailView
from django.core.urlresolvers import reverse

class DetailViewBase(DetailView):
	url_name = "" # line 2
		
class DetailViewCustom(DetailViewBase):
	template_name = 'base/cbv/cbv/DetailViewCustom.html' # line 1
	def get_success_url(self): # line 3
		return reverse(self.success_url)
	def get_context_data(self, **kwargs): # line 4
		context = super(DetailViewCustom, self).get_context_data(**kwargs) # line 5
		model_name = self.model._meta.verbose_name.title() # line 6
		context['model_name'] = model_name # line 7
		context['url_name'] = self.url_name # line 8
		return context