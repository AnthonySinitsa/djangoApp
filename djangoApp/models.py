from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class DjangoApp(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField(default='1. #Todo goes here')
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('djangoApp_detail', args=[str(self.id)])
