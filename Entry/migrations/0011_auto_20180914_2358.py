# Generated by Django 2.1.1 on 2018-09-14 15:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0010_auto_20180914_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 14, 15, 58, 49, 733065, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 14, 15, 58, 49, 733065, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_like',
            field=models.IntegerField(default=0),
        ),
    ]
