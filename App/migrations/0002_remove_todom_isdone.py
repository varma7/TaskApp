# Generated by Django 3.1.4 on 2020-12-23 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todom',
            name='IsDone',
        ),
    ]
