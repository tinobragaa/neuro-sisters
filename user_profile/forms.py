from django import forms

class EditProfileForm(forms.Form):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))