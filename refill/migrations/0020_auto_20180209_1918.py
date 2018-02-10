# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0019_auto_20180209_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug_refill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(blank=True, max_length=50)),
                ('drug_dose', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='refill',
            name='Dr_Phone_number',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='Dr_adrress',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='Dr_name',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='choose_your_shipment_method',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='last_pharmacy',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='last_pharmacy_adrress',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='prescription',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='vedrify_with_Pharmacy',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='verify_with_DR',
        ),
        migrations.RemoveField(
            model_name='refill',
            name='verify_with_prescription',
        ),
        migrations.AddField(
            model_name='newrx',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='refill',
            name='Date_of_Birth',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refill',
            name='RX_number',
            field=models.CharField(blank=True, help_text='optional', max_length=20),
        ),
        migrations.AddField(
            model_name='refill',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='refill',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='refill',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='drug_refill',
            name='med',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='refill.Refill'),
        ),
    ]
