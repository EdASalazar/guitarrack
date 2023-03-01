# Generated by Django 4.1.7 on 2023-03-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('color', models.CharField(max_length=100)),
                ('numPickups', models.IntegerField()),
                ('typePickups', models.CharField(max_length=200)),
            ],
        ),
    ]
