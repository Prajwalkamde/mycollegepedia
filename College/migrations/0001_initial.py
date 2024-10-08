# Generated by Django 4.2.8 on 2023-12-27 06:02

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Exam', '0001_initial'),
        ('Main', '0001_initial'),
        ('Auth', '0001_initial'),
        ('General', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('city', models.CharField(max_length=70, verbose_name='city')),
                ('current_address', models.TextField(blank=True, verbose_name='current address')),
                ('permanent_address', models.TextField(blank=True, verbose_name='permanent address')),
                ('zipcode', models.IntegerField(null=True, verbose_name='zipcode')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='meta title')),
                ('keyword', models.TextField(blank=True, null=True, verbose_name='meta keywords')),
                ('description', models.TextField(blank=True, null=True, verbose_name='meta description')),
                ('name', models.CharField(error_messages={'unique': 'This college is already exists.'}, max_length=255, unique=True, verbose_name='College name')),
                ('rank', models.PositiveIntegerField(verbose_name='college rank')),
                ('logo', models.ImageField(upload_to='college/logo')),
                ('image', models.ImageField(upload_to='college/image')),
                ('established_year', models.IntegerField(verbose_name='established year')),
                ('overview', ckeditor.fields.RichTextField(verbose_name='overview')),
                ('admission_process', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='admission process')),
                ('specialization', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Specialization')),
                ('career', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Career')),
                ('opportunity', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Opportunity')),
                ('scope', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Scope')),
                ('brochure', models.FileField(blank=True, upload_to='college/brochure')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name', unique=True)),
                ('college_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.collegetype')),
                ('college_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Auth.collegeadmin')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.country')),
                ('course_category', models.ManyToManyField(to='General.coursecategory')),
                ('organization_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.organizationtype')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.state')),
            ],
            options={
                'verbose_name': 'College',
                'verbose_name_plural': 'Colleges',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('question', models.CharField(max_length=200, verbose_name='questions')),
                ('answer', ckeditor.fields.RichTextField(verbose_name='answer')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq', to='College.college')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Eligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('eligibility', models.CharField(blank=True, max_length=255, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('application_start_date', models.DateField(max_length=8, null=True, verbose_name='application start date')),
                ('application_end_date', models.DateField(max_length=8, null=True, verbose_name='application end date')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.category')),
                ('college', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eligibility', to='College.college')),
                ('course_stream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='General.coursestream')),
                ('course_subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='General.coursesubcategory')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.exam')),
            ],
            options={
                'verbose_name': 'Eligibility',
                'verbose_name_plural': 'Eligibility',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='CourseFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('year_fees', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='year fees')),
                ('total_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='total fees')),
                ('academic_year', models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.CASCADE, to='General.academicyear')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_fee', to='College.college')),
                ('course_stream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='General.coursestream')),
                ('course_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.coursesubcategory')),
            ],
            options={
                'verbose_name': 'Course Fee',
                'verbose_name_plural': 'Course Fees',
            },
        ),
        migrations.CreateModel(
            name='CollegeGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='college/gallery')),
                ('alt', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='College.college')),
            ],
            options={
                'verbose_name': 'College Gallery',
                'verbose_name_plural': 'College Gallery',
            },
        ),
        migrations.CreateModel(
            name='CollegeApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='College.college')),
                ('course_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.coursecategory')),
                ('course_stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.coursestream')),
                ('course_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.coursesubcategory')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.student')),
            ],
            options={
                'verbose_name': 'College Application',
                'verbose_name_plural': 'College Applications',
                'ordering': ['-updated_at'],
            },
        ),
    ]
