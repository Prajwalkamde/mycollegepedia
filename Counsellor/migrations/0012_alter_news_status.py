# Generated by Django 4.2.8 on 2024-05-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Counsellor', '0011_alter_news_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('PUBLIC', 'PUBLIC')], max_length=10),
        ),
    ]
