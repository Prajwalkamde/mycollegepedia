# Generated by Django 4.2.8 on 2024-02-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0024_alter_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('PUBLIC', 'PUBLIC')], max_length=10),
        ),
    ]
