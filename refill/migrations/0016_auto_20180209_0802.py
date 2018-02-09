# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-09 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20180208_1744'),
        ('refill', '0015_auto_20180208_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewRx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('verify_with_DR', models.BooleanField(default=False)),
                ('Dr_name', models.CharField(blank=True, help_text='only required if verifying with dr is selected', max_length=50)),
                ('Dr_Phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('Dr_adrress', models.CharField(blank=True, max_length=100)),
                ('vedrify_with_Pharmacy', models.BooleanField(default=False)),
                ('last_pharmacy', models.CharField(blank=True, max_length=100)),
                ('last_pharmacy_adrress', models.CharField(blank=True, max_length=100)),
                ('verify_with_prescription', models.BooleanField(default=False)),
                ('prescription', models.ImageField(blank=True, upload_to='')),
                ('more_refill', models.BooleanField(default=False)),
                ('more_refill_number', models.CharField(blank=True, max_length=20)),
                ('choose_your_shipment_method', models.CharField(choices=[('p', 'pick-up'), ('d', 'deliver')], default='d', max_length=1)),
                ('info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='info_user', to='user_profile.UserInfo')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterField(
            model_name='drug',
            name='med',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='refill.NewRx'),
        ),
    ]
