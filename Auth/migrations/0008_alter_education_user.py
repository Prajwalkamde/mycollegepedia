# Generated by Django 4.2.8 on 2024-02-17 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0007_alter_passwordresettoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='Auth.student'),
        ),
    ]
