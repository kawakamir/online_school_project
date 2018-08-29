# Generated by Django 2.1 on 2018-08-29 04:01

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20180826_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='joined_at',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2018, 8, 29))], verbose_name='受講日'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_category',
            field=models.IntegerField(choices=[(0, '英語'), (1, 'プログラミング'), (2, 'ファイナンス')], verbose_name='ジャンル'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_time',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='受講時間'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Person', verbose_name='受講者'),
        ),
    ]
