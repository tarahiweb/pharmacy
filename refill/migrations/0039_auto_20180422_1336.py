# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-22 13:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0038_auto_20180422_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='newrxasqeust',
            name='Phone_number',
            field=models.CharField(blank=True, default='111111111111', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='newrxasqeust',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='newrxasqeust',
            name='first_name',
            field=models.CharField(default='user', max_length=50),
        ),
        migrations.AlterField(
            model_name='newrxasqeust',
            name='last_name',
            field=models.CharField(default='user', max_length=50),
        ),
    ]