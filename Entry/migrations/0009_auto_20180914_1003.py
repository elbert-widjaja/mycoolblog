# Generated by Django 2.1.1 on 2018-09-14 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0008_auto_20180912_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 14, 2, 3, 27, 854022, tzinfo=utc)),
        ),
    ]
