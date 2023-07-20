from django.urls import path
from .views import AppListView, AppDetailView, AppCreateView, AppUpdateView, AppDeleteView

urlpatterns = [
  path('', AppListView.as_view(), name='djangoApp_list'),
  path('<int:pk>/', AppDetailView.as_view(), name='djangoApp_detail'),
  path('create/', AppCreateView.as_view(), name='djangoApp_create'),
  path('<int:pk>/update/', AppUpdateView.as_view(), name='djangoApp_update'),
  path('<int:pk>/delete/', AppDeleteView.as_view(), name='djangoApp_delete'),
]