# Generated by Django 5.0.2 on 2024-02-21 20:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_with_me', '0003_alter_student_options_alter_student_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='university_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='university_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
