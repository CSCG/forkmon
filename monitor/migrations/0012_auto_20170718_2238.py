# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_auto_20170718_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='mtp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]