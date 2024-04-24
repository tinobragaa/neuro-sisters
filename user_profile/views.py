from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect

from blog.models import Friendship, Post
from user_profile.models import UserProfile


def get_user_profile(user_id):
    return UserProfile.objects.get(user__id=user_id)


def get_user(user_id):
    return User.objects.get(id=user_id)


def get_friends(user_id):
    return Friendship.objects.filter(user_id=user_id)


@login_required
def display_user_profile(request):
    user_id = request.user.id
    profile = get_user_profile(user_id)
    # user = get_user(user_id)
    friends = get_friends(user_id)
    context = {'user_profile': profile,
               'friends': friends}

    return render(request, 'user_profile/profile.html',
                  context)


@login_required
def display_friend_profile(request, user_id):

    profile = get_user_profile(user_id)
    user = get_user(request.user.id)
    posts = Post.objects.filter(author_id=user_id)

    context = {'user_profile': profile,
               'posts': posts}

    return render(request, 'user_profile/friends_profile.html',
                  context)



@login_required
def add_friend(request, user_id):
    user_one = get_user(request.user.id)
    user_two = get_user(user_id)
    if user_one != user_two:
        friendship, created = Friendship.objects.get_or_create(
            user_id=user_one.id, friend_id=user_id)
        if created:
            context = {'message': 'Friend Added Successfully'}
        else:
            context = {'message': 'Already friends'}
    else:
        context = {'message': 'You cannot add yourself as a friend'}
        return render(request, 'user_profile/profile.html', context)
    return redirect('profile')
    # return render(request, 'user_profile/friends_profile.html', context)


def remove_friend(request, friend_id):
    friendship = Friendship.objects.get(id=friend_id)
    friendship.delete()
    return redirect('profile')
