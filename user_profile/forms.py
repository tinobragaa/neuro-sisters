from profile import Profile

from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from user_profile.models import UserProfile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["bio"]
        widgets = {
            "bio": CKEditor5Widget(attrs={"class": "django_ckeditor_5"},
                                   config_name="default")
        }
