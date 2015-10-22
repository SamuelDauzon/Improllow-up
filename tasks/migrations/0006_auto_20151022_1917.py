# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20151018_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('modified', models.DateTimeField(verbose_name='Date de modification', auto_now=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nom du type de tâche')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(verbose_name='Type de tâche', to='tasks.TaskType'),
        ),
    ]
