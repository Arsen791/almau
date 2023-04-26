# Generated by Django 4.1.2 on 2023-04-19 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info1', '0018_remove_professor_year_of_appropriation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': [('is_dean', 'Декан')]},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('PR', 'Преподаватель'), ('DE', 'Декан')], default='ST', max_length=2),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
