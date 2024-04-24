from django.urls import path

from user_profile.views import (display_user_profile,
                                display_friend_profile,
                                add_friend, remove_friend)

urlpatterns = [
    path('', display_user_profile, name='profile'),
    path('friend/<int:friend_id>', display_friend_profile, name='friend_profile'),
    path('friend/add/<int:user_id>', add_friend, name='add_friend'),
    path('friend/remove/<int:friend_id>', remove_friend, name='remove_friend'),
]
