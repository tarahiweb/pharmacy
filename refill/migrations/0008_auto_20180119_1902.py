# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 01:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0007_auto_20180118_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=100)),
                ('drug_dose', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='refill',
            name='drug_dose',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='drug_name',
        ),
        migrations.AddField(
            model_name='drug',
            name='med',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='refill.Refill'),
        ),
    ]
