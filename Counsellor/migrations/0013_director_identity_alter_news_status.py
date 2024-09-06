# Generated by Django 4.2.8 on 2024-05-27 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Counsellor', '0012_alter_news_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='identity',
            field=models.CharField(choices=[('Aadhar', 'Aadhar Card'), ('Pan', 'Pan Card'), ('Voter', 'Voter ID'), ('Driving', 'Driving License'), ('Passport', 'Passport')], default='Aadhar', max_length=10, verbose_name='identity'),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('DRAFT', 'DRAFT')], max_length=10),
        ),
    ]
