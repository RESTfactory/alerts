# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='owner',
        ),
    ]
