# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='predicted_end_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='total_time',
            field=models.SmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='end_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
