# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-25 05:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20170624_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='be_or_me',
            new_name='course',
        ),
    ]