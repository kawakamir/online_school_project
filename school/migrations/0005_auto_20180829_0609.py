# Generated by Django 2.1 on 2018-08-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20180829_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='joined_at',
            field=models.DateField(verbose_name='受講日'),
        ),
    ]
