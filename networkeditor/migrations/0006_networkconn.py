# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 07:31
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkeditor', '0005_auto_20161110_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='networkconn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkid', models.TextField()),
                ('Lat', models.FloatField()),
                ('Long', models.FloatField()),
                ('ConnectedPoints', django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), size=None)),
            ],
        ),
    ]