from django.urls import path

from blog.views import blog_home, submit_comment, post_detail_view

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('comments/submit/<int:post_id>', submit_comment, name='submit_comment'),
    path('detail/<int:post_id>', post_detail_view, name='post_detail'),
]
