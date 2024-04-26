from django.urls import path
from django.conf.urls import handler404, handler500, handler403


from blog.views import (blog_home,
                        submit_comment,
                        post_detail_view,
                        remove_comment,
                        edit_comment,
                        edit_post,
                        add_post,
                        reaction_add,
                        custom_404,
                        custom_500,
                        custom_403)

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('comments/submit/<int:post_id>', submit_comment, name='submit_comment'),
    path('detail/<int:post_id>', post_detail_view, name='post_detail'),
    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('comments/delete/<int:comment_id>', remove_comment, name='delete_comment'),
    path('edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('reaction/add/<int:post_id>/<reaction_type>', reaction_add, name='add_reaction'),
]


handler404 = custom_404
handler500 = custom_500
handler403 = custom_403
