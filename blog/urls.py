from django.urls import path

from blog.views import (blog_home,
                        submit_comment,
                        post_detail_view,
                        remove_comment)

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('comments/submit/<int:post_id>', submit_comment, name='submit_comment'),
    path('detail/<int:post_id>', post_detail_view, name='post_detail'),
    path('comments/delete/<int:comment_id>', remove_comment, name='delete_comment'),
]
