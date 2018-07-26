# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0008_auto_20170523_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='treasury_receipt_number',
        ),
        migrations.AlterField(
            model_name='application',
            name='no_of_floors',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='application',
            name='registration_plan_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='sn',
            field=models.IntegerField(default=0),
        ),
    ]
