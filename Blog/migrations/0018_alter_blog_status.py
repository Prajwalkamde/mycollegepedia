# Generated by Django 4.2.8 on 2024-01-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0017_alter_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('DRAFT', 'DRAFT')], max_length=10),
        ),
    ]
