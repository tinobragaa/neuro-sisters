from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from .forms import EditProfileForm

from blog.models import Friendship, Post
from user_profile.models import UserProfile
from django.contrib import messages

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
    friends = get_friends(user_id)
    context = {'user_profile': profile,
               'friends': friends}

    return render(request, 'user_profile/profile.html',
                  context)


@login_required
def display_friend_profile(request, friend_id):

    profile = get_user_profile(friend_id)
    user = get_user(request.user.id)
    posts = Post.objects.filter(author_id=friend_id)

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
            messages.success(request, 'Friend Added Successfully')

        else:
            context = {'message': 'Already friends'}
            messages.warning(request, 'Already friends')

    else:
        context = {'message': 'You cannot add yourself as a friend'}
        messages.warning(request, 'You cannot add yourself as a friend')

        return render(request, 'user_profile/profile.html', context)
    return redirect('profile')


def remove_friend(request, friend_id):
    friendship = Friendship.objects.get(id=friend_id)
    friendship.delete()
    messages.success(request, 'Friend Removed Successfully')

    return redirect('profile')


@login_required
def edit_profile(request):
    user_profile = get_user_profile(request.user.id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            user_profile.bio = bio
            user_profile.save()
            messages.success(request, 'Bio updated successfully')
            return redirect('profile')
    else:
        form = EditProfileForm(initial={'bio': user_profile.bio})
    
    return render(request, 'user_profile/edit_profile.html', {'form': form})