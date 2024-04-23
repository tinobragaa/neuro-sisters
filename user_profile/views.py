from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render

from blog.models import Friendship
from user_profile.models import UserProfile


def get_user_profile(user_id):
    return UserProfile.objects.get(user__id=user_id)


def get_user(user_id):
    return User.objects.get(id=user_id)


def get_friends(user_id):
    return Friendship.objects.filter(user_id=user_id)


def display_user_profile(request):
    user_id = request.user.id
    profile = get_user_profile(user_id)
    # user = get_user(user_id)
    friends = get_friends(user_id)
    context = {'user_profile': profile,
               'friends': friends}

    return render(request, 'user_profile/profile.html',
                  context)
