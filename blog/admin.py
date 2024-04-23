from django.contrib import admin

# Register your models here.
from blog.models import (Post, Comment, Category, Reactions, Friendship,
                         UserProfile)

# admin.site.register(Post)
# admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Reactions)
admin.site.register(Friendship)
admin.site.register(UserProfile)


class ReactionsAdminInline(admin.StackedInline):
    model = Reactions


class CommentAdminInline(admin.StackedInline):
    model = Comment
    extra = 0
    classes = ['collapse']


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentAdminInline]


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    inlines = [ReactionsAdminInline]