# Generated by Django 4.2.8 on 2024-05-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Counsellor', '0008_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsellor',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('DRAFT', 'DRAFT')], max_length=10),
        ),
    ]
