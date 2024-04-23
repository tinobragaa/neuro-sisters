from django.urls import path

from user_profile.views import display_user_profile

urlpatterns = [
    path('', display_user_profile, name='profile'),

]
