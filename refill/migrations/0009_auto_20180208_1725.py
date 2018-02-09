# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-08 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0008_auto_20180119_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refill',
            name='choose_your_shipment_method',
            field=models.CharField(choices=[('p', 'pick-up'), ('d', 'deliver')], default='p', max_length=15),
        ),
    ]
