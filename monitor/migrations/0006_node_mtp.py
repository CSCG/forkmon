# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 05:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_auto_20170718_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='mtp',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 18, 22, 35, 26, 608327)),
        ),
    ]