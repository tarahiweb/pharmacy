# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-17 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0025_merge_20180216_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug_refill',
            name='drug_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
