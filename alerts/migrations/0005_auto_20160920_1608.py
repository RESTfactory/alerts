# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_auto_20160920_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerttype',
            name='description',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='entitytype',
            name='description',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]