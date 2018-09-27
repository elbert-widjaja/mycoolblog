# Generated by Django 2.1.1 on 2018-09-12 09:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0007_auto_20180911_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 12, 9, 18, 19, 196093, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]