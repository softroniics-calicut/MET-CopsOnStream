# Generated by Django 4.2.6 on 2024-02-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cops_app', '0005_alter_case_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Case_ongoing', 'Case_ongoing'), ('Case_Incomplete', 'Case_incomplete'), ('Case_solved/closed', 'Case_solved/closed')], max_length=50, null=True),
        ),
    ]