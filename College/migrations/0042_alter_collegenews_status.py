# Generated by Django 4.2.8 on 2024-05-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0041_alter_collegenews_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegenews',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('PUBLIC', 'PUBLIC')], max_length=10),
        ),
    ]
