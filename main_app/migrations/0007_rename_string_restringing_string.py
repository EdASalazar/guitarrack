# Generated by Django 4.1.7 on 2023-03-02 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_restring_restringing_string_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restringing',
            old_name='String',
            new_name='string',
        ),
    ]
