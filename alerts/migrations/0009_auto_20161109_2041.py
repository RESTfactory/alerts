# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0008_auto_20161102_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]