# Generated by Django 4.2.8 on 2023-12-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0003_alter_eligibility_application_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='rank',
            field=models.PositiveIntegerField(unique=True, verbose_name='college rank'),
        ),
    ]
