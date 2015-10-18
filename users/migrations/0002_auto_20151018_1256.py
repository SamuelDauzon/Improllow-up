# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Supérieur hiérarchique', related_name='user_boss'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hiring_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name="Date d'arrivée"),
        ),
    ]
