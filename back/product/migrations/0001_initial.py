# Generated by Django 4.1.3 on 2022-11-01 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assingment',
            fields=[
                ('assingment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='lecture',
            fields=[
                ('lecture_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='problem',
            fields=[
                ('problem_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('restriction', models.TextField()),
                ('reference', models.TextField()),
                ('timelimit', models.IntegerField()),
                ('memorylimit', models.IntegerField()),
                ('assingment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.assingment')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('role', models.TextField()),
                ('created_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='user_lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.user')),
            ],
        ),
        migrations.CreateModel(
            name='testcase',
            fields=[
                ('testcase_id', models.AutoField(primary_key=True, serialize=False)),
                ('idx', models.IntegerField()),
                ('isHidden', models.BooleanField()),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.problem')),
            ],
        ),
        migrations.CreateModel(
            name='solution',
            fields=[
                ('solution_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField()),
                ('modified_date', models.DateField()),
                ('answer_code', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.problem')),
            ],
        ),
        migrations.CreateModel(
            name='code',
            fields=[
                ('code_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField()),
                ('modified_date', models.DateField()),
                ('code_idx', models.IntegerField()),
                ('user_code', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.user')),
            ],
        ),
        migrations.CreateModel(
            name='session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField()),
                ('submission_count', models.IntegerField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.user')),
            ]
        ),
        migrations.AddField(
            model_name='assingment',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.lecture'),
        ),
    ]
