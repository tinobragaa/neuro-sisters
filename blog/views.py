from datetime import timezone, datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from blog.forms import CommentForm, PostForm
from blog.models import Post, Category, Reactions, Comment, Friendship

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.admin.views.decorators import staff_member_required


def get_post(post_id):
    """
    :param post_id: The ID of the post to retrieve.
    :return: The post object with the specified ID.
    """
    return get_object_or_404(Post, pk=post_id)


def blog_home(request):
    """
    Render the blog home page.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered blog home page.
    :rtype: HttpResponse
    """
    posts = Post.objects.all()
    categories = Category.objects.all()
    comment_form = CommentForm()
    friends_list = []
    if request.user.is_authenticated:
        friends_list = [friend.friend.id for friend in Friendship.objects.filter(user=request.user)]

    context = {
        'posts': posts,
        'categories': categories,
        'comment_form': comment_form,
        'friends_list': friends_list,
    }

    return render(request, 'blog/blog.html', context)


# submit comment
@login_required
def submit_comment(request, post_id):
    """
    :param request: The HTTP request object.
    :param post_id: The ID of the post the comment belongs to.
    :return: A HttpResponseRedirect object if the form is valid and the comment is submitted successfully, else a rendered HTML page with the comment form.

    """
    # Only process form data on POST
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.objects.get(pk=post_id)
            comment.save()
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post_id}))
    # If not a POST, or the form isn't valid, render the form again with the
    # existing information
    return render(request,
                  'blog/blog.html',
                  {'form': CommentForm()})


def post_detail_view(request, post_id):
    """
    :param request: A HttpRequest object representing the request made by the client
    :param post_id: An integer representing the ID of the post to be viewed
    :return: A rendered HttpResponse object

    This function takes in a request and a post_id and retrieves the post with the given ID using the `get_post` function. It also retrieves the comments for the post using the `Comment.objects.filter` method. The function then creates a context dictionary with the post, comments, and a CommentForm instance. Finally, it renders the 'blog/post_detail.html' template with the context and returns the rendered response.
    """
    post = get_post(post_id)
    comments = Comment.objects.filter(post_id=post.id)
    context = {
        'post': post,
        'comments': comments,
        'comment_form': CommentForm()
    }

    return render(request, 'blog/post_detail.html', context)


@login_required
@staff_member_required
def remove_comment(request, comment_id):
    """
    Removes a comment.

    :param request: the HTTP request object.
    :type request: ~django.http.HttpRequest
    :param comment_id: the ID of the comment to be removed.
    :type comment_id: int
    :return: an HTTP response redirecting to the post detail page.
    """
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment Removed Successfully')

    return HttpResponseRedirect(reverse('post_detail',
                                        kwargs={'post_id': comment.post.id}))


@login_required
@staff_member_required
def remove_category(request, category_id):
    """
    :param request: The request object.
    :param category_id: The ID of the category to be removed.
    :return: The HTTP response redirecting to the 'profile' page.
    """
    category = Category.objects.get(pk=category_id)
    category.delete()
    messages.success(request, 'Category Removed Successfully')

    return HttpResponseRedirect(reverse('profile'))


@login_required
@staff_member_required
def remove_post(request, post_id):
    """
    :param request: The HTTP request object.
    :param post_id: The ID of the post to be removed.
    :return: None
      """
    post = get_post(post_id)
    post.delete()
    messages.success(request, 'Post Removed Successfully')

    return HttpResponseRedirect(reverse('profile'))


@login_required
@staff_member_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.content = request.POST.get('content', '')
            post.updated_at = datetime.now()
            post.save()
        return HttpResponseRedirect(reverse('blog_home'))
    else:
        form = PostForm()
        return render(request, 'blog/add_post.html', {'form': form})


@login_required
@staff_member_required
def edit_post(request, post_id):
    """
    Edit a post.

    :param request: The HTTP request object.
    :param post_id: The ID of the post to be edited.
    :return: If the request method is 'POST', the function updates the content of the post with the value of 'content' from the request's POST data, saves the post, and redirects to the post detail page. Otherwise, it renders the 'blog/edit_post.html' template with the 'post' context variable.

    """
    post = get_post(post_id)
    # form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.author = request.user
            form.updated_at = datetime.now()
            print(form.cleaned_data)
            form.save()
            messages.success(request, 'Post Edited Successfully')
        return HttpResponseRedirect(reverse('post_detail',
                                            kwargs={'post_id': post_id}))
    else:
        form = PostForm(instance=post)
        return render(request,
                      'blog/edit_post.html',
                      {'post': post, 'form': form})


@login_required
@staff_member_required
def edit_comment(request, comment_id):
    """
    Edits a comment.

    :param request: The HTTP request.
    :type request: HttpRequest
    :param comment_id: The ID of the comment to be edited.
    :return: If the request method is POST and the form is valid, the user will be redirected to the 'post_detail' page of the comment's associated post. Otherwise, it will render the 'edit_comment.html' template with the comment form.

    """
    comment = Comment.objects.get(pk=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': comment.post.id}))
    else:
        form = CommentForm(instance=comment)

    return render(request,
                  'blog/edit_comment.html',
                  {'form': form})


def reaction_add(request, post_id):
    reaction_type = request.POST.get('reaction_type')
    # post_id = request.POST.get('post_id')
    post = get_post(post_id)
    reaction = Reactions.objects.create(post=post, user=request.user,
                                        reaction_type=reaction_type)
    reaction.save()
    return HttpResponseRedirect(
        reverse('post_detail', kwargs={'post_id': post_id}))



def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)


def custom_500(request):
    return render(request, 'errors/500.html', status=500)


def custom_403(request, exception):
    return render(request, 'errors/403.html', status=403)