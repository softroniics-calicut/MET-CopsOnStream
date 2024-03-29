# Generated by Django 4.2.6 on 2024-02-01 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cops_app', '0004_alter_case_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Case ongoing', 'Case ongoing'), ('Case Incomplete', 'Case incomplete'), ('Case solved/closed', 'Case solved/closed')], max_length=50, null=True),
        ),
    ]
