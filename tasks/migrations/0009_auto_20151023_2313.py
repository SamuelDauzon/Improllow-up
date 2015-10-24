# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20151023_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(to='projects.Project', verbose_name='Projet', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(to='tasks.TaskType', verbose_name='Type de tâche', null=True, blank=True),
        ),
    ]
