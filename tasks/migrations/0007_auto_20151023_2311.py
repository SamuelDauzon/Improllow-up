# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20151022_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(verbose_name='Type de tâche', default=None, to='tasks.TaskType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(verbose_name='Projet', to='projects.Project'),
        ),
    ]
