# Generated by Django 4.1.3 on 2022-11-02 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_assingment_problem_assignment_problem_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='reference',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='restriction',
            field=models.TextField(null=True),
        ),
    ]