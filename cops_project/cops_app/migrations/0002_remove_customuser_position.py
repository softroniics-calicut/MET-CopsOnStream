# Generated by Django 4.2.6 on 2024-01-31 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cops_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='position',
        ),
    ]
