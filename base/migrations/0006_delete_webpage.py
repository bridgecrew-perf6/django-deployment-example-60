# Generated by Django 4.0.1 on 2022-02-02 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_webpage_alter_room_options_remove_room_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]
