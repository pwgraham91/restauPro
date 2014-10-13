# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0007_auto_20141010_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='number_of_children',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='party',
            name='number_of_females',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='party',
            name='number_of_males',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='party',
            name='party_name',
            field=models.CharField(help_text=b'enter this if you know the name of the party so you can save their data', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='total_time',
            field=models.CharField(max_length=2, blank=True),
        ),
    ]
