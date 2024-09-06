# Generated by Django 4.2.8 on 2023-12-30 06:55

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
