# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 23:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0002_auto_20180116_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refill',
            name='user',
        ),
    ]
