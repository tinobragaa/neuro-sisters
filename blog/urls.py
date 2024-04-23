from django.urls import path

from blog.views import blog_home, submit_comment

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('comments/submit/<int:post_id>', submit_comment, name='submit_comment')
]
