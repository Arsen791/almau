# Generated by Django 4.1.2 on 2023-04-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info1', '0010_alter_doctor_doctor_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_profile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
