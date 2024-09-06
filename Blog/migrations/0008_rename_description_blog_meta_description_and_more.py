# Generated by Django 4.2.8 on 2023-12-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_alter_blog_image_alter_blog_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='description',
            new_name='meta_description',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='keyword',
            new_name='meta_keyword',
        ),
        migrations.AddField(
            model_name='blog',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='meta title'),
        ),
    ]
