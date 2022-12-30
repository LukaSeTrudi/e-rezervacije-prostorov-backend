# Generated by Django 4.1.3 on 2022-12-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0013_alter_courtschedule_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='courtschedule',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='courtscheduleexception',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='courtschedule',
            name='day',
            field=models.CharField(choices=[('3', 'Wednesday'), ('6', 'Saturday'), ('1', 'Monday'), ('7', 'Sunday'), ('4', 'Thursday'), ('2', 'Tuesday'), ('5', 'Friday')], max_length=1),
        ),
    ]
