# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0011_auto_20170528_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='profile_photo',
            field=models.FileField(default='profile_photo', upload_to='profile_photo'),
        ),
    ]