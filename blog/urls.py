from django.urls import path

from blog.views import (blog_home,
                        submit_comment,
                        post_detail_view,
                        remove_comment,
                        edit_comment,
                        edit_post)

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('comments/submit/<int:post_id>', submit_comment, name='submit_comment'),
    path('detail/<int:post_id>', post_detail_view, name='post_detail'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('comments/delete/<int:comment_id>', remove_comment, name='delete_comment'),
    path('edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
]
