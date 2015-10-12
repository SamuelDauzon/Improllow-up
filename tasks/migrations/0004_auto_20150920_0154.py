# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='details',
            field=models.TextField(verbose_name='Détails', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.IntegerField(blank=True, verbose_name='Durée', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='execution_date',
            field=models.DateField(blank=True, verbose_name="Date d'éxecution", null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(verbose_name='Nom de la tâche', max_length=128),
        ),
        migrations.AlterField(
            model_name='task',
            name='user_add',
            field=models.ForeignKey(verbose_name='Ajoutée par', to=settings.AUTH_USER_MODEL, related_name='user_add', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='userprofile',
            field=models.ForeignKey(verbose_name='Effectuée par', to=settings.AUTH_USER_MODEL, related_name='userprofile', blank=True, null=True),
        ),
    ]
