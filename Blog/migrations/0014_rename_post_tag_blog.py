# Generated by Django 4.2.8 on 2024-01-13 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_alter_blog_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='post',
            new_name='blog',
        ),
    ]
