# Generated by Django 5.0.1 on 2024-01-28 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('typelodgings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typelodging',
            name='image',
        ),
    ]
