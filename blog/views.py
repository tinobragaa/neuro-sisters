from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Post, Category

from django.http import HttpResponseRedirect
from django.urls import reverse


def blog_home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'categories': categories,
        'comment_form': comment_form,
    }
    return render(request, 'blog/blog.html', context)


# submit comment
def submit_comment(request, post_id):
    # Only process form data on POST
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_id)
            comment.save()
            return HttpResponseRedirect(reverse('blog_home'))

    # If not a POST, or the form isn't valid, render the form again with the existing information
    return render(request, 'blog/blog.html', {'form': CommentForm()})
