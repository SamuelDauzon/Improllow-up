# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user_add',
            field=models.ForeignKey(verbose_name='Ajoutée par', related_name='user_add', to=settings.AUTH_USER_MODEL, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='userprofile',
            field=models.ForeignKey(verbose_name='Effectuée par', related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
