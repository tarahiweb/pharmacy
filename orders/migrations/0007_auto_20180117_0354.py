# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20180113_2038'),
        ('orders', '0006_auto_20180117_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='usinfo',
        ),
        migrations.AddField(
            model_name='order',
            name='info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='info', to='user_profile.UserInfo'),
        ),
    ]
