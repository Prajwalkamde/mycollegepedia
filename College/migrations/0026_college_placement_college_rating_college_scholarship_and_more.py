# Generated by Django 4.2.8 on 2024-02-21 09:48

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0025_alter_admissionblog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='placement',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='placement'),
        ),
        migrations.AddField(
            model_name='college',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='Enter a rating between 0.0 and 5.0', max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='rating'),
        ),
        migrations.AddField(
            model_name='college',
            name='scholarship',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Scholarship'),
        ),
        migrations.AlterField(
            model_name='admissionblog',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('PUBLIC', 'PUBLIC')], max_length=10),
        ),
    ]
