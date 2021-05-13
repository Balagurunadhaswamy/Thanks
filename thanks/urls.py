from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('home', TemplateView.as_view(template_name='index.html')),
    path('save-data', views.index, name='index'),
    path('', views.home, name='home'),
    path('last',views.last, name='last'),
]