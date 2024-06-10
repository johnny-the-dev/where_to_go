# Generated by Django 4.2.13 on 2024-06-08 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description_short', models.CharField(max_length=200)),
                ('description_long', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceCoordinate',
            fields=[
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='places.place')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='places.place')),
            ],
        ),
    ]