# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0006_auto_20141010_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='predicted_end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='reservation_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='total_time',
            field=models.SmallIntegerField(null=True),
        ),
    ]
