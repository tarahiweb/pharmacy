# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-02 01:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0006_auto_20180119_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug_emergency_drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(blank=True, max_length=50)),
                ('drug_dose', models.CharField(blank=True, max_length=20)),
                ('drug_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emergency_as_guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('Date_of_Birth', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='drug_emergency_drug',
            name='med',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='emergency.Emergency_as_guest'),
        ),
    ]