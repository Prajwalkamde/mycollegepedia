# Generated by Django 4.2.8 on 2023-12-27 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-id'], 'verbose_name': 'About Us', 'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-id'], 'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterModelOptions(
            name='privacypolicy',
            options={'ordering': ['-id'], 'verbose_name': 'Privacy Policy', 'verbose_name_plural': 'Privacy Policy'},
        ),
        migrations.AlterModelOptions(
            name='siteconfig',
            options={'ordering': ['-id'], 'verbose_name': 'Site Config', 'verbose_name_plural': 'Site Config'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['-title'], 'verbose_name': 'Slider', 'verbose_name_plural': 'Slider'},
        ),
    ]
