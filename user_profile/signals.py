from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from user_profile.models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # The bio field is not set because the User instance has not bio attribute by default.
        # But you can still update this attribute with the profile detail form.
        UserProfile.objects.create(user=instance)
