# Generated by Django 5.1.2 on 2024-10-27 15:20

import django_mysql.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_profile_score1_alter_profile_score2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='score1',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=255, size=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score2',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=255, size=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score3',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=255, size=10),
        ),
    ]
