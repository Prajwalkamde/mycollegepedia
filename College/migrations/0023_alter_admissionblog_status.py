# Generated by Django 4.2.8 on 2024-02-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0022_collegevideo_videourl_alter_collegevideo_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionblog',
            name='status',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('DRAFT', 'DRAFT')], max_length=10),
        ),
    ]
