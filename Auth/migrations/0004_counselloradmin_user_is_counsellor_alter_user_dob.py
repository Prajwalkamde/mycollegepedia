# Generated by Django 4.2.8 on 2024-01-16 09:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_alter_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounsellorAdmin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('brand_name', models.CharField(max_length=255, verbose_name='brand name')),
                ('company_certificate', models.FileField(upload_to='counsellor/company', verbose_name='company certificate')),
                ('gst', models.CharField(blank=True, help_text='Special characters are not allowed', max_length=15, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9\\s]*$', message='GST Number must be Alphanumeric!!!'), django.core.validators.MaxLengthValidator(15, 'GST Number must be 15 digits!!!'), django.core.validators.MinLengthValidator(15, 'GST Number must be have at least 15 digits!!!')], verbose_name='GST Number')),
                ('pancard', models.CharField(blank=True, help_text='Special characters are not allowed', max_length=10, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9\\s]*$', message='Pan Card Number must be Alphanumeric!!!'), django.core.validators.MaxLengthValidator(10, 'Pan Card Number must be 10 digits!!!'), django.core.validators.MinLengthValidator(10, 'Pan Card Number must be have at least 10 digits!!!')], verbose_name='Pan Card Number')),
            ],
            options={
                'verbose_name': 'Company User',
                'verbose_name_plural': 'Company Users',
                'ordering': ['-id'],
            },
            bases=('Auth.user',),
        ),
        migrations.AddField(
            model_name='user',
            name='is_counsellor',
            field=models.BooleanField(default=False, help_text='Designates whether the counsellor can log into this admin site.', verbose_name='counsellor status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, max_length=8, null=True, verbose_name='date of birth'),
        ),
    ]
