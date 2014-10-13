# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0003_party_reservation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='x_position',
            field=models.SmallIntegerField(default=0, help_text=b'grid'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='table',
            name='y_position',
            field=models.SmallIntegerField(default=0, help_text=b'grid'),
            preserve_default=True,
        ),
    ]
