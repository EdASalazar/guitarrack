# Generated by Django 4.1.7 on 2023-03-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_cat_restringing_guitar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restringing',
            old_name='restring',
            new_name='String',
        ),
        migrations.AlterField(
            model_name='restringing',
            name='date',
            field=models.DateField(verbose_name='Date Changed'),
        ),
    ]
