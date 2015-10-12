# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='Date de création', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Date de modification', auto_now=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=128)),
                ('duration', models.IntegerField(verbose_name='Durée')),
                ('execution_date', models.DateField(verbose_name="Date d'éxecution")),
                ('project', models.ForeignKey(verbose_name='Projet', to='projects.Project')),
                ('userprofile', models.ForeignKey(verbose_name='Effectuée par', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
    ]
