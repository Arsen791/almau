# Generated by Django 4.1.2 on 2023-04-19 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info1', '0017_remove_master_magistr_specialization_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='year_of_appropriation',
        ),
    ]
