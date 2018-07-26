# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.IntegerField(default=0)),
                ('applicant', models.CharField(max_length=250)),
                ('location_of_proposal', models.CharField(max_length=250)),
                ('registration_plan_number', models.CharField(max_length=20)),
                ('type_of_use', models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Recreational', 'Recreational'), ('Industrial', 'Industrial'), ('Mixeduse', 'Mixeduse')], max_length=15)),
                ('no_of_floors', models.IntegerField(max_length=2)),
                ('amount', models.IntegerField(max_length=10)),
                ('treasury_receipt_number', models.IntegerField(max_length=8)),
                ('name_of_inspector', models.CharField(max_length=25)),
                ('name_of_recommending_officer', models.CharField(max_length=20)),
                ('name_of_charting_officer', models.CharField(max_length=20)),
                ('name_of_approving_officer', models.CharField(max_length=20)),
                ('luc_no', models.CharField(max_length=10)),
            ],
        ),
    ]
