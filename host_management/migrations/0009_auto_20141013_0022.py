# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0008_auto_20141010_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='dinner',
        ),
        migrations.RemoveField(
            model_name='party',
            name='friday_to_sunday',
        ),
        migrations.AlterField(
            model_name='party',
            name='lunch',
            field=models.BooleanField(default=False, help_text=b'check true for lunch or false for dinner'),
        ),
        migrations.AlterField(
            model_name='party',
            name='monday_to_thursday',
            field=models.BooleanField(default=False, help_text=b'check true for Monday to Thursday or false for Friday to Sunday'),
        ),
    ]
