# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-19 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0032_auto_20180318_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='newrx',
            name='shiping_method',
            field=models.CharField(choices=[('7.5', 'express one day shiping $7.5'), ('0', 'regular three day shiping')], default='0', max_length=50),
        ),
    ]