# Generated by Django 4.1.3 on 2022-11-01 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='assingment',
            new_name='assignment',
        ),
        migrations.RenameField(
            model_name='assignment',
            old_name='assingment_id',
            new_name='assignment_id',
        ),
    ]