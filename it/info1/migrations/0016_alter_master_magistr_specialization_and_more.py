# Generated by Django 4.1.2 on 2023-04-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info1', '0015_master_magistr_specialization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='magistr_specialization',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='master',
            name='magistr_year_of_graduation',
            field=models.IntegerField(default=' '),
        ),
    ]
