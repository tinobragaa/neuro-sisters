from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """

    UserProfile Model
    -----------------

    This class represents a user profile in the application.
    It contains the user's information such as username, bio, and profile picture.

    Attributes:
    -----------
    - user (OneToOneField): The user associated with the profile.
    - bio (CKeditor RichTextField): The user's biography.

    Methods:
    --------
    - __str__(): Returns the username of the user.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = CKEditor5Field('Bio', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username

