# Generated by Django 2.2 on 2019-07-02 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenanceapp', '0006_auto_20190701_0501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintenancechecklist',
            old_name='desription',
            new_name='description',
        ),
    ]
