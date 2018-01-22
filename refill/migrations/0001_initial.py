# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 07:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0005_auto_20180113_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refill',
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
                ('prescription', models.ImageField(blank=True, upload_to='')),
                ('more_refill', models.BooleanField(default=False)),
                ('info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inf', to='user_profile.UserInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refill', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]