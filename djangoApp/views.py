from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import DjangoApp
from django.urls import reverse_lazy

class AppListView(ListView):
  template_name = 'djangoApp-list.html'
  model = DjangoApp
  # context_object_name = 'ToDo_list'
  
class AppDetailView(DetailView):
  template_name = 'djangoApp-detail.html'
  model = DjangoApp
  
class AppCreateView(CreateView):
  template_name = 'djangoApp-create.html'
  model = DjangoApp
  fields = ['title', 'body', 'author']
  
class AppUpdateView(UpdateView):
  template_name = 'djangoApp-update.html'
  model = DjangoApp
  fields = ['id', 'title', 'body', 'author']
  
class AppDeleteView(DeleteView):
  template_name = 'djangoApp-delete.html'
  model = DjangoApp
  success_url = reverse_lazy('djangoApp_list')