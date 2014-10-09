# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0002_auto_20141009_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='reservation_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
