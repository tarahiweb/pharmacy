# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-08 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalspa', '0002_auto_20180408_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='Medical_spa_name',
        ),
        migrations.AddField(
            model_name='compound',
            name='City',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='compound',
            name='Email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='compound',
            name='First_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='compound',
            name='Last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='compound',
            name='State',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='compound',
            name='Zip',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
