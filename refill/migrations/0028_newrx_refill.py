# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-19 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0027_drug_drug_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='newrx',
            name='refill',
            field=models.BooleanField(default=False),
        ),
    ]
