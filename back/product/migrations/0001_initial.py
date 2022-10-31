# Generated by Django 4.1.2 on 2022-10-31 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.CharField(max_length=200)),
                ('problem_name', models.TextField()),
                ('description', models.TextField()),
                ('restriction', models.TextField()),
                ('test_case', models.IntegerField()),
            ],
        ),
    ]