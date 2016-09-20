# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0003_remove_app_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerttype',
            name='app',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='alerts.App'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entitytype',
            name='app',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='alerts.App'),
            preserve_default=False,
        ),
    ]