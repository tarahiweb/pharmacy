# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-07 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='drug_pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
