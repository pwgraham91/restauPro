# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0005_auto_20141010_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
