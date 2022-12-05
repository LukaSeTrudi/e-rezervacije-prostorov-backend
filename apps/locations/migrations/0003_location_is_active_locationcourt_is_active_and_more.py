# Generated by Django 4.1.3 on 2022-12-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_rename_owner_id_location_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='locationcourt',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='locationcourt',
            name='is_outside',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='locationcourt',
            name='court_types',
            field=models.ManyToManyField(blank=True, related_name='court_types', to='locations.courttype'),
        ),
    ]