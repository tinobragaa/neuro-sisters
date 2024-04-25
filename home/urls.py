from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('read_more/', views.read_more, name='read_more'),

]
