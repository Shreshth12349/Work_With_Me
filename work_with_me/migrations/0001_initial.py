# Generated by Django 5.0.2 on 2024-02-21 11:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('university_name', models.CharField(max_length=100)),
                ('university_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('skills', models.ManyToManyField(to='work_with_me.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('skills_required', models.ManyToManyField(to='work_with_me.skill')),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_with_me.user')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('application_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('application_date_time', models.DateTimeField(auto_now=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_with_me.project')),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_with_me.user')),
            ],
        ),
    ]
