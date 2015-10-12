# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150920_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='details',
            field=models.TextField(default=None, verbose_name='Détails'),
            preserve_default=False,
        ),
    ]
