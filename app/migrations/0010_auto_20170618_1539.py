# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-18 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20170618_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='aadhar_number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='college_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='diploma_board',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='diploma_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='pan_number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='passport_number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='prn',
            field=models.CharField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_yeargap_reason',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelveth_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]