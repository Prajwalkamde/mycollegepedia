# Generated by Django 4.2.8 on 2023-12-30 12:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Terms & Condition',
                'verbose_name_plural': 'Terms & Condition',
                'ordering': ['-id'],
            },
        ),
    ]
