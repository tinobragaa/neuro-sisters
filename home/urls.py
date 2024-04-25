from django.urls import path
from .views import read_more, about, index

urlpatterns = [
    path('', index, name='home'),
    path('read_more/', read_more, name='read_more'),
    path('about/', about, name='about'),

]
