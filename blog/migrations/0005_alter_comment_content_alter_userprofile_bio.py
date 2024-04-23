# Generated by Django 5.0.4 on 2024-04-23 18:48

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Add a Comment'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Bio'),
        ),
    ]
