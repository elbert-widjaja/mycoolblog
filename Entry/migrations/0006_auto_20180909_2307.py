# Generated by Django 2.1.1 on 2018-09-09 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0005_auto_20180909_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 15, 7, 23, 775009, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='registered_at',
            field=models.DateTimeField(),
        ),
    ]