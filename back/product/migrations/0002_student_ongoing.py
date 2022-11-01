# Generated by Django 4.1.3 on 2022-11-01 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('student_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ongoing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.problem')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.student')),
            ],
        ),
    ]
