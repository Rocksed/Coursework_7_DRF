# Generated by Django 4.2.3 on 2023-08-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atomic_habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time_to_complete',
            field=models.TimeField(verbose_name='время на выполнение '),
        ),
    ]