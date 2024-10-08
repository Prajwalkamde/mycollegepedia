# Generated by Django 4.2.8 on 2024-05-03 05:27

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0033_news_delete_admissionblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default=True, upload_to='college/news', verbose_name='thumbnail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]
