# Generated by Django 4.1.3 on 2022-11-30 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='owner_id',
            new_name='owner',
        ),
    ]