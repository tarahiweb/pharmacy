# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-22 13:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0037_remove_refill_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugQeust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(blank=True, max_length=100)),
                ('drug_dose', models.CharField(blank=True, max_length=20)),
                ('drug_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewRxAsQeust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('Date_of_Birth', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('delivered', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('cansel', models.BooleanField(default=False)),
                ('Dr_name', models.CharField(blank=True, help_text='only required if verifying with dr is selected', max_length=50)),
                ('dr_phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('Dr_adrress', models.CharField(blank=True, max_length=100)),
                ('last_pharmacy', models.CharField(blank=True, max_length=100)),
                ('last_pharmacy_adrress', models.CharField(blank=True, max_length=100)),
                ('prescription', models.ImageField(blank=True, upload_to='')),
                ('rx_number', models.CharField(max_length=10, null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='drugqeust',
            name='med',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drug_qeust', to='refill.NewRxAsQeust'),
        ),
    ]
