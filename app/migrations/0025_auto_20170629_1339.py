# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-29 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20170629_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='be_outof',
            field=models.IntegerField(default=0),
        ),
    ]
