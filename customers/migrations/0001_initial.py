# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='Date de création', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Date de modification', auto_now=True)),
                ('corporate_name', models.CharField(verbose_name='Nom', max_length=255)),
            ],
            options={
                'abstract': False,
                'ordering': ('-created',),
            },
        ),
    ]
