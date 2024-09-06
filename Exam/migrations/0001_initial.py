# Generated by Django 4.2.8 on 2023-12-27 06:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('title', models.CharField(max_length=255, verbose_name='exam title')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='exam description')),
                ('full_form', models.CharField(blank=True, max_length=200, null=True, verbose_name='full form')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UpcomingExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('image', models.ImageField(upload_to='exam/upcoming')),
                ('exam_mode', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default='Online', max_length=20, verbose_name='exam mode')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='exam description')),
                ('exam_start_date', models.DateField(blank=True, null=True, verbose_name='exam start date')),
                ('exam_end_date', models.DateField(blank=True, null=True, verbose_name='exam end date')),
                ('application_start_date', models.DateField(blank=True, null=True, verbose_name='application form start date')),
                ('application_end_date', models.DateField(blank=True, null=True, verbose_name='application form end date')),
                ('result', models.DateField(blank=True, null=True, verbose_name='result date')),
                ('url', models.URLField(blank=True, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.exam')),
            ],
            options={
                'verbose_name': 'Upcoming Exam',
                'verbose_name_plural': 'Upcoming Exams',
                'ordering': ['-id'],
            },
        ),
    ]
