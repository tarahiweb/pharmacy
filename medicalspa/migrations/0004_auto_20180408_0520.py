# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-08 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalspa', '0003_auto_20180408_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compound',
            name='First_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='compound',
            name='Last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]