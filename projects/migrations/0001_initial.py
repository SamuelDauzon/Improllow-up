# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='Date de création', auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('name', models.CharField(max_length=127, verbose_name='Nom')),
                ('customer', models.ForeignKey(verbose_name='Client', to='customers.Customer')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
    ]
