# Generated by Django 3.1.3 on 2020-11-22 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_stuff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuff',
            name='image',
        ),
    ]
