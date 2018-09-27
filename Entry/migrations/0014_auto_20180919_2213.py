# Generated by Django 2.1.1 on 2018-09-19 14:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0013_auto_20180919_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 19, 14, 13, 42, 644602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 19, 14, 13, 42, 645604, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 19, 14, 13, 42, 644602, tzinfo=utc)),
        ),
    ]
