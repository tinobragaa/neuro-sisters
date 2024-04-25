from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', ]
        widgets = {
            'content': CKEditor5Widget(attrs={"class": "django_ckeditor_5"},
                                       config_name="default")
        }


class CommentForm(forms.ModelForm):
    """Form for comments to the article."""
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["content"].required = False

    class Meta:
        model = Comment
        exclude = ('author', 'post')
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
                config_name="default"

            )
        }
