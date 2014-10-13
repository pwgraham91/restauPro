# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0004_auto_20141010_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='table',
            new_name='seated_table',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='restaurant',
            new_name='premise',
        ),
        migrations.RemoveField(
            model_name='party',
            name='weekday',
        ),
        migrations.AddField(
            model_name='party',
            name='dinner',
            field=models.BooleanField(default=False, help_text=b'check true for dinner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='friday_to_sunday',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='monday_to_thursday',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='lunch',
            field=models.BooleanField(default=False, help_text=b'check true for lunch'),
        ),
    ]
