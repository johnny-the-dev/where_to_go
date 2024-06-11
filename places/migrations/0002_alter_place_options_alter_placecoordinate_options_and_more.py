# Generated by Django 4.2.13 on 2024-06-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Локация', 'verbose_name_plural': 'Локации'},
        ),
        migrations.AlterModelOptions(
            name='placecoordinate',
            options={'verbose_name': 'Координаты', 'verbose_name_plural': 'Координаты'},
        ),
        migrations.AlterModelOptions(
            name='placeimage',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AddField(
            model_name='placeimage',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер картинки'),
        ),
    ]
