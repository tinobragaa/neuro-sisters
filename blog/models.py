from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


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
    bio = CKEditor5Field('Text')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username


class Friendship(models.Model):
    """
    Friendship/followers

    A class representing a friendship between two users.
     It enables one to follow another, and read each others created posts.

    Attributes:
        user (User): The user who initiated the friendship.
        friend (User): The user who is the friend in the friendship.
        created_at (DateTime): The date and time when the friendship was created.

    Methods:
        None

    Usage:
        friendship = Friendship.objects.create(user=user1, friend=user2)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_friendship')

    friend = models.ManyToManyField(User, related_name='friendship')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} friend with {', '.join([str(friend) for friend in self.friend.all()])}"


class Category(models.Model):
    """
    Model class for representing a category.

    Attributes:
        name (str): The name of the category.

    Methods:
        __str__(): Returns a string representation of the category.

    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    """
        Post class represents a blog post.

        Attributes:
            title (CharField): The title of the blog post.
            content (TextField): The content of the blog post.
            category (ForeignKey): The category of the blog post.
            created_at (DateTimeField): The date and time of when the blog post was created.
            updated_at (DateTimeField): The date and time of when the blog post was last updated.

        Methods:
            __str__(): Returns a string representation of the blog post.

    """
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    content = CKEditor5Field('Text')
    category = models.ManyToManyField(Category, related_name='post_categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Comment(models.Model):
    """

    This class represents a comment made on a post.

    Attributes:
        author (str): The name of the author of the comment.
        content (str): The content of the comment.
        post (Post): The post to which the comment belongs.
        created_at (datetime): The date and time when the comment was created.
        updated_at (datetime): The date and time when the comment was last updated.

    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = CKEditor5Field('Add a Comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Created on: {self.created_at.strftime('%d.%m.%y : %H.%M')} "


class Reactions(models.Model):
    """
    The Reactions class represents a model for storing reactions to posts in a social media application.

    Attributes:
        REACTION_CHOICES (list): List of tuples representing the available reaction choices.
        Each tuple contains a reaction constant and its corresponding display value.

        reaction (CharField): CharField representing the selected reaction.
        It is limited to a maximum length of 10 and can take one of the values defined in REACTION_CHOICES. The default value is 'Like'.

        post (ForeignKey): ForeignKey to the Post model, specifying a one-to-many relationship.
        The reaction is associated with a specific post and will be deleted if the post is deleted.

        user (ForeignKey): ForeignKey to the User model, specifying a one-to-many relationship.
        The reaction is associated with a specific user and will be deleted if the user is deleted.
    """
    LIKE = 'LIKE'
    LOVE = 'LOVE'
    HAHA = 'HAHA'
    WOW = 'WOW'
    SAD = 'SAD'
    ANGRY = 'ANGRY'

    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (LOVE, 'Love'),
        (HAHA, 'Haha'),
        (WOW, 'Wow'),
        (SAD, 'Sad'),
        (ANGRY, 'Angry'),
    ]
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES,
                                default=LIKE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reaction'
        verbose_name_plural = 'Reactions'
        unique_together = ['post', 'user']
        ordering = ['-created_at']

    def get_reaction_count(self):
        return Reactions.objects.filter(post=self.post).count()

    def __str__(self):
        return self.reaction
