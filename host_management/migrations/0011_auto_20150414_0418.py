# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0010_auto_20141013_0528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='seated_table',
            new_name='table',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='premise',
            new_name='restaurant',
        ),
        migrations.RemoveField(
            model_name='table',
            name='x_position',
        ),
        migrations.RemoveField(
            model_name='table',
            name='y_position',
        ),
    ]
