from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import DjangoApp
from django.urls import reverse_lazy

class AppListView(ListView):
  model = DjangoApp
  template_name = 'djangoApp-list.html'
  context_object_name = 'djangoApp'
  
class AppDetailView(DetailView):
  model = DjangoApp
  template_name = 'djangoApp-detail.html'
  
class AppCreateView(CreateView):
  model = DjangoApp
  template_name = 'djangoApp-create.html'
  fields = ['title', 'body', 'author']
  
class AppUpdateView(UpdateView):
  model = DjangoApp
  template_name = 'djangoApp-update.html'
  fields = ['title', 'body']
  
class AppDeleteView(DeleteView):
  model = DjangoApp
  template_name = 'djangoApp-delete.html'
  success_url = reverse_lazy('djangoApp_list')