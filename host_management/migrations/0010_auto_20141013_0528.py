# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0009_auto_20141013_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='party_name',
            field=models.CharField(help_text=b'Enter this if you know the name of the party so you can save their data', max_length=50, blank=True),
        ),
    ]
