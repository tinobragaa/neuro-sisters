# Generated by Django 5.0.4 on 2024-04-23 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_content_alter_userprofile_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]