# Generated by Django 4.1.3 on 2022-12-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_alter_courtschedule_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courtschedule',
            name='day',
            field=models.CharField(choices=[('1', 'Monday'), ('4', 'Thursday'), ('2', 'Tuesday'), ('7', 'Sunday'), ('5', 'Friday'), ('3', 'Wednesday'), ('6', 'Saturday')], max_length=1),
        ),
    ]