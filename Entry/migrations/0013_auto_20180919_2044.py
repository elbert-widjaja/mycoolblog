# Generated by Django 2.1.1 on 2018-09-19 12:44

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0012_auto_20180915_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2018, 9, 19, 12, 43, 55, 30575, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 19, 12, 43, 55, 30575, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 19, 12, 43, 55, 30575, tzinfo=utc)),
        ),
    ]
