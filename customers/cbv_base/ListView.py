# coding: utf-8
from django.views.generic.list import ListView

class ListViewBase(ListView):
	url_name = ""
	# Gérer template_name pour mobile
		
class ListViewCustom(ListViewBase):
	paginate_by = 10 
	template_name = 'base/templates/cbv/base/ListViewCustom.html'
	def get_success_url(self):
		return reverse(self.success_url)
	def get_context_data(self, **kwargs):
		context = super(ListViewCustom, self).get_context_data(**kwargs)
		model_name = self.model._meta.verbose_name.title()
		context['model_name'] = model_name
		return context

class ListViewCustomOrderBy(ListViewBase):
	cbv_order_by = ""
	paginate_by = 10
	url_delete_name = ""
	url_update_name = ""
	url_create_name = ""
	url_detail_name = ""
	url_list_name = ""
	template_name = 'base/templates/cbv/base/ListViewCustom.html'
	def get_success_url(self):
		return reverse(self.success_url)
	def get_context_data(self, **kwargs):
		context = super(ListViewCustomOrderBy, self).get_context_data(**kwargs)
		model_name = self.model._meta.verbose_name.title()
		model_fields = self.model._meta.get_all_field_names()
		context['model_name'] = model_name
		context['url_update_name'] = self.url_update_name
		context['url_create_name'] = self.url_create_name
		context['url_delete_name'] = self.url_delete_name
		context['url_list_name'] = self.url_list_name
		context['url_detail_name'] = self.url_detail_name
		context['model_fields'] = model_fields
		return context
	# Méthode pour trier différement les ListView. Voir pour ajouter un dictionnaire qui montre les champs sur lesquels on peut trier.
	def get_queryset(self):
		self.queryset = super(ListViewCustomOrderBy, self).get_queryset()
		if self.request.GET:
			if 'cbv_order_by_listview' in self.request.GET:
				self.cbv_order_by = self.request.GET.get('cbv_order_by_listview', '')
		if self.cbv_order_by!="":
			self.queryset=self.queryset.order_by(self.cbv_order_by)
		return self.queryset
