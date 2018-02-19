# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20180219_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shiping_method',
            field=models.CharField(choices=[('e == 7.5', 'express one day shiping $7.5'), ('r == 0', 'regular three day shiping')], default='r', max_length=50),
        ),
    ]
