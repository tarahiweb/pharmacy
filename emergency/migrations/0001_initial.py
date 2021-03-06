# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0005_auto_20180113_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency_Med',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('Dr_name', models.CharField(max_length=50)),
                ('Dr_Phone_number', models.IntegerField(null=True)),
                ('Dr_adrress', models.CharField(max_length=100)),
                ('last_pharmacy', models.CharField(max_length=100)),
                ('last_pharmacy_adrress', models.CharField(max_length=100)),
                ('drug_name', models.CharField(max_length=100)),
                ('drug_dose', models.CharField(max_length=20)),
                ('drug_name1', models.CharField(blank=True, max_length=100)),
                ('drug_dose1', models.CharField(blank=True, max_length=20)),
                ('drug_name2', models.CharField(blank=True, max_length=100)),
                ('drug_dose2', models.CharField(blank=True, max_length=20)),
                ('prescription', models.ImageField(blank=True, upload_to='')),
                ('info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emergencyinfo', to='user_profile.UserInfo')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
