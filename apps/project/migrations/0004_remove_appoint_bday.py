# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 04:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20170427_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoint',
            name='bday',
        ),
    ]
