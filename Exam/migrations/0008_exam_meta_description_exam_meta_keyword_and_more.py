# Generated by Django 4.2.8 on 2024-01-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0007_rename_keyword_upcomingexam_meta_keyword_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='exam',
            name='meta_keyword',
            field=models.TextField(blank=True, null=True, verbose_name='meta keywords'),
        ),
        migrations.AddField(
            model_name='exam',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='meta title'),
        ),
    ]
