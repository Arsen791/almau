# Generated by Django 4.1.2 on 2023-04-12 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info1', '0005_rename_criminal_criminal_criminal_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_number', models.IntegerField()),
                ('medicine_date', models.DateField(null=True)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='info1.user_name')),
            ],
            options={
                'verbose_name': 'Medicine',
                'verbose_name_plural': 'Medicines',
            },
        ),
    ]