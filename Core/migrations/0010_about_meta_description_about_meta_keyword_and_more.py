# Generated by Django 4.2.8 on 2024-01-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_alter_contact_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='about',
            name='meta_keyword',
            field=models.TextField(blank=True, null=True, verbose_name='meta keywords'),
        ),
        migrations.AddField(
            model_name='about',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='meta title'),
        ),
        migrations.AddField(
            model_name='contact',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='contact',
            name='meta_keyword',
            field=models.TextField(blank=True, null=True, verbose_name='meta keywords'),
        ),
        migrations.AddField(
            model_name='contact',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='meta title'),
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='meta_keyword',
            field=models.TextField(blank=True, null=True, verbose_name='meta keywords'),
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='meta title'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='meta_keyword',
            field=models.TextField(blank=True, null=True, verbose_name='meta keywords'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='meta title'),
        ),
        migrations.AddField(
            model_name='termsandcondition',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='termsandcondition',
            name='meta_keyword',
            field=models.TextField(blank=True, null=True, verbose_name='meta keywords'),
        ),
        migrations.AddField(
            model_name='termsandcondition',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='meta title'),
        ),
    ]
