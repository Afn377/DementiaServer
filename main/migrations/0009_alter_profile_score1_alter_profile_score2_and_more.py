# Generated by Django 5.1.2 on 2024-10-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_profile_score1_alter_profile_score2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='score1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score2',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score3',
            field=models.CharField(default='', max_length=255),
        ),
    ]
