# Generated by Django 4.2.13 on 2024-06-11 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_placeimage_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['-place__title', 'number'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]