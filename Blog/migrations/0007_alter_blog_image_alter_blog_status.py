# Generated by Django 4.2.8 on 2023-12-30 07:15

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='blog', verbose_name='blog image'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('DRAFT', 'DRAFT')], max_length=10),
        ),
    ]
