# Generated by Django 4.2.8 on 2024-01-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0011_collegevideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionblog',
            name='status',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('DRAFT', 'DRAFT')], max_length=10),
        ),
    ]
