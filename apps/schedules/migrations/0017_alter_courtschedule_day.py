# Generated by Django 4.1.3 on 2023-01-04 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0016_alter_courtschedule_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courtschedule',
            name='day',
            field=models.CharField(choices=[('6', 'Saturday'), ('3', 'Wednesday'), ('1', 'Monday'), ('2', 'Tuesday'), ('7', 'Sunday'), ('5', 'Friday'), ('4', 'Thursday')], max_length=1),
        ),
    ]
