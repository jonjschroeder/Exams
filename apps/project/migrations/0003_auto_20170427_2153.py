# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170427_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='time',
            field=models.TimeField(),
        ),
    ]