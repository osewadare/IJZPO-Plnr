# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0012_staff_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(choices=[('Inspector', 'Inspector'), ('Recommending Officer', 'Recommending Officer'), ('Charting Officer', 'Charting Officer'), ('Approving Officer', 'Approving Officer'), ('Others', 'Others'), ('Corpers', 'Corpers')], default='Others', max_length=100),
        ),
    ]
