# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-06 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20180306_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shiping_method',
            field=models.CharField(choices=[('7.5', 'express one day shiping $7.5'), ('0', 'regular three day shiping')], default='0', max_length=50),
        ),
    ]
