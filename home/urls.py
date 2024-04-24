from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('read_more/', views.index, name='read_more'),

]
