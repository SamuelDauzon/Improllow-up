# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20150920_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.PositiveIntegerField(verbose_name='Durée', null=True, blank=True),
        ),
    ]
