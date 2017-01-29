# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 03:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0008_auto_20170126_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorithm', models.CharField(max_length=100)),
                ('distance', models.FloatField(default=0.0)),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Query')),
            ],
        ),
    ]
