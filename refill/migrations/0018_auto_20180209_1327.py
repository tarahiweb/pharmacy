# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-09 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0017_auto_20180209_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='newrx',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='newrx',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
